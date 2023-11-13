from utils import FileReader, get_combinations, all_equal, convert_to_int

import qiskit.qasm2
from abc import ABC, abstractmethod
from qiskit import QuantumCircuit, QuantumRegister, Aer
from qiskit.quantum_info import schmidt_decomposition
from qiskit_aer.backends import StatevectorSimulator
from qiskit_aer.backends.compatibility import Statevector
from qiskit.result import Result
from qiskit.converters import circuit_to_dag
from qiskit.dagcircuit import DAGCircuit
from qiskit.circuit.quantumcircuit import BitLocations, Qubit
from qiskit.circuit.library import XGate, RYGate, HGate, CXGate, SwapGate
from io import TextIOWrapper
from copy import deepcopy
from math import pi


class PatternDetector(ABC):

    def __init__(self, program: TextIOWrapper) -> None:
        self.program: TextIOWrapper = program
        self.circuit: QuantumCircuit = None

    def load_circuit(self, program: TextIOWrapper) -> None:
        program_str: str = program.read()
        self.program.seek(0)

        # Workaround to find all possible gates due to a bug in qiskit's current parser.
        self.circuit: QuantumCircuit = qiskit.qasm2.loads(
            program_str, 
            include_path=qiskit.qasm2.LEGACY_INCLUDE_PATH,
            custom_instructions=qiskit.qasm2.LEGACY_CUSTOM_INSTRUCTIONS,
            custom_classical=qiskit.qasm2.LEGACY_CUSTOM_CLASSICAL
        )

    @abstractmethod
    def build_message(self) -> str:
        pass


class UniformSuperpositionDetector(PatternDetector):

    def __init__(self, program: TextIOWrapper) -> None:
        super().__init__(program)
        self.load_circuit(self.program)

    def build_message(self) -> str:

        in_ufs: bool = True
        message: str = ""
        reader: FileReader = FileReader(self.program)
        program_len: int = len(self.program.readlines())
        self.program.seek(0)

        # Read input line after line.
        for line_num in range(0, program_len):
            current_program: str = reader.read_file_until(line_num)
            self.circuit = qiskit.qasm2.loads(current_program)

            # Circuit with depth of 0 cannot be in uniform superposition.
            if self.circuit.depth() == 0:
                if in_ufs:
                    message += ("Uniform Superposition: Quantum state is not in uniform superposition"
                                "from line {ln} onwards.\n").format(ln=line_num)
                    in_ufs = False
                continue

            # Calculate the state vector of the circuit.
            backend: StatevectorSimulator = Aer.get_backend('statevector_simulator')
            result: Result = backend.run(self.circuit).result()
            outputstate: Statevector = result.get_statevector(self.circuit)

            # Calculate state probabilities and check if they are all equal. Ancilla bits, that do not have to be in
            # superposition, are also taken into account.
            prob: list = outputstate.probabilities()
            binary_combinations: list = self._calc_all_binary_combinations(self.circuit.num_qubits)

            state_combinations: list = list(get_combinations(range(0, self.circuit.num_qubits)))
            state_combinations.pop()

            found: bool = False
            for state in state_combinations:
                c_binary_combinations: list = deepcopy(binary_combinations)
                filtered_states: list = self._filter_indices(c_binary_combinations, state)

                if all_equal(prob, convert_to_int(filtered_states)):
                    if not in_ufs:
                        message += ("Uniform Superposition: Quantum state is in uniform superposition"
                                    "from line {ln} onwards.\n").format(ln=line_num)
                        in_ufs = True

                    found = True
                    break

            if found:
                found = False
                continue

            if in_ufs:
                in_ufs = False
                message += ("Uniform Superposition: Quantum state is not in uniform superposition"
                            "from line {ln} onwards.\n").format(ln=line_num)

        return message.strip()

    def _calc_all_binary_combinations(self, n: int) -> list:
        result: list = []
        for i in range(1 << n):
            # Convert the current number to a binary string of length n
            binary_str = format(i, '0' + str(n) + 'b')
            result.append(binary_str)

        return result

    def _filter_indices(self, binary_list: list, index_list: list):
        list_copy: list = deepcopy(binary_list)
        to_delete: list = []
        elem_count: int = 0
        for i in range(0, len(binary_list)):
            for index in index_list:
                if binary_list[i][index] != '0':
                    to_delete.append(i-elem_count)
                    elem_count += 1
                    break

        for i in to_delete:
            list_copy.pop(i)

        return list_copy


class EntanglementDetector(PatternDetector):

    def __init__(self, program: TextIOWrapper) -> None:
        super().__init__(program)

    def build_message(self) -> str:
        is_entangled: bool = True
        message: str = ""
        reader: FileReader = FileReader(self.program)
        program_len: int = len(self.program.readlines())
        self.program.seek(0)

        # Read input file line after line.
        for line_num in range(0, program_len):
            current_program: str = reader.read_file_until(line_num)
            self.circuit = qiskit.qasm2.loads(current_program)

            if self.circuit.depth() == 0:
                if is_entangled:
                    message += "Creating Entanglement: Quantum state is not entangled from line {ln} onwards.\n"\
                        .format(ln=line_num)
                    is_entangled = False
                continue

            # Calculate the state vector of the circuit.
            backend: StatevectorSimulator = Aer.get_backend('statevector_simulator')
            result: Result = backend.run(self.circuit).result()
            outputstate: Statevector = result.get_statevector(self.circuit)

            # Determines if a quantum state is entangled using Schmidt decomposition.
            combinations: list = list(get_combinations(range(0, self.circuit.num_qubits)))[1:-1]
            found: bool = False
            for comb in combinations:
                decomp: list = schmidt_decomposition(outputstate, comb)

                schmidt_coefficents: list = []
                for decomp_elem in decomp:
                    if decomp_elem[0] > 0:
                        schmidt_coefficents.append(decomp_elem[0])

                # Number of posititve Schmidt coefficients is called the Schmidt-rank of the state vector.
                # The quantum state is entangled iff the Schmidt-rank is greater than 1.
                if len(schmidt_coefficents) > 1:
                    if not is_entangled:
                        message += "Creating Entanglement: Quantum state is entangled from line {ln} onwards.\n"\
                            .format(ln=line_num)
                        is_entangled = True
                    found = True
                    break

            if found:
                found = False
                continue

            if is_entangled:
                is_entangled = False
                message += "Creating Entanglement: Quantum state is not entangled from line {ln} onwards.\n"\
                    .format(ln=line_num)

        return message.strip()


class BasisEncodingDetector(PatternDetector):
    
    def __init__(self, program: TextIOWrapper) -> None:
        super().__init__(program)
        self.load_circuit(self.program)

    # Search for Pauli-X gates in the first layer.
    def build_message(self) -> str:
        
        message: str = ""
        encoded_nums: dict = {}
        dag: DAGCircuit = circuit_to_dag(self.circuit)

        for node in dag.front_layer():
            if node.name == XGate().name:
                qubit: Qubit = node.qargs[0]
                location: BitLocations = self.circuit.find_bit(qubit)
                register: QuantumRegister = location.registers[0][0]
                index: int = location.registers[0][1]
                
                if register in encoded_nums:
                    encoded_nums[register].append(index)
                else:
                    encoded_nums[register] = [index]

        for reg, index_list in encoded_nums.items():
            decimal: int = self._bin_index_to_decimal(index_list, reg.size)
            message += "Basis Encoding: Value {num} is encoded in quantum register {reg}.\n"\
                .format(num=decimal, reg=reg.name)
            
        return message.strip()
        

    def _bin_index_to_decimal(self, index_list: list, num_of_qubits: int) -> int:

        binary_list: list = []
        for qubit in range(0, num_of_qubits):
            if qubit in index_list:
                binary_list.append(1)
            else:
                binary_list.append(0)
        
        return sum(val*(2**idx) for idx, val in enumerate(binary_list))


class AngleEncodingDetector(PatternDetector):

    def __init__(self, program: TextIOWrapper) -> None:
        super().__init__(program)
        self.load_circuit(self.program)

    # Search for R_y gates in the first layer.
    def build_message(self) -> str:
        message: str = ""
        dag: DAGCircuit = circuit_to_dag(self.circuit)

        for node in dag.front_layer():
            # Angle has to satisfy normalization constraint.
            if node.name == RYGate(0).name and node.op.params[0] < pi:
                qubit: Qubit = node.qargs[0]
                location: BitLocations = self.circuit.find_bit(qubit)
                register: QuantumRegister = location.registers[0][0]
                message += "Angle Encoding: Qubit {qubit} in quantum register {reg} is used for angle encoding.\n"\
                    .format(qubit=location.index, reg=register.name)

        return message.strip()


class AmplitudeEncodingDetector(PatternDetector):
    
    # There are many methods for creating amplitude encoding which makes it difficult to detect.
    pass


class PhaseEstimationDetector(PatternDetector):

    def __init__(self, program: TextIOWrapper) -> None:
        super().__init__(program)
        self.load_circuit(self.program)

    # Search for the special circuit used for PhaseEstimation.
    def build_message(self) -> str:
        dag: DAGCircuit = circuit_to_dag(self.circuit)

        # Stores bits in unifrom superposition with the corresponding gates.
        # key: possible gate and the bits it operates on
        # value: list of hadamard transformed bits
        hadamards: dict = {}

        found_u: bool = False

        # Iterate through all layers of the circuit.
        for layer in dag.layers():

            # First iteration to fing u gates.
            for node in layer['graph'].front_layer():

                qubit: Qubit = node.qargs[0]
                location: BitLocations = self.circuit.find_bit(qubit)
                qubit_index: int = location.index

                # Look for U gates.
                if node.op.num_qubits > 1:
                    found_u = True
                    operating_bits: list = []
                    for i in range(1, len(node.qargs)):
                        o_qubit: Qubit = node.qargs[i]
                        location: BitLocations = self.circuit.find_bit(o_qubit)
                        operating_bits.append(location.index)

                    for key, value in hadamards.copy().items():
                        if qubit_index not in value:
                            del hadamards[key]
                            continue

                        # Save gate name and the operating qubits in key.
                        current_key: str = repr((node.name, operating_bits))
                        if key == "": 
                            hadamards[current_key] = hadamards.pop("")
                            hadamards[current_key].remove(qubit_index)
                            continue

                        if key != current_key:
                            del hadamards[key]
                            continue

                        hadamards[key].remove(qubit_index)

            if not found_u:
                hadamards.clear()

            found_u = False

            # Second iteration for adding Hadamard transformed qubits.
            for node in layer['graph'].front_layer():   
                if node.name == HGate().name:

                    qubit: Qubit = node.qargs[0]
                    location: BitLocations = self.circuit.find_bit(qubit)
                    qubit_index: int = location.index

                    if "" in hadamards.keys():
                        hadamards[""].append(qubit_index)
                        continue

                    hadamards[""] = [qubit_index]

            # If all ancillary bits are used, an instance of the pattern has been found.
            for value in hadamards.values():
                if not value:
                    return "Quantum Phase Estimation: Instance of Quantum Phase Estimation detected."


class UncomputeDetector(PatternDetector):
    
    def __init__(self, program: TextIOWrapper) -> None:
        super().__init__(program)
        self.load_circuit(self.program)

    def build_message(self) -> str:

        dag: DAGCircuit = circuit_to_dag(self.circuit)

        # Stores all bit pairs where a cx gate has been applied to.
        # key: control bit
        # value: operating bit
        cx_nodes: dict = {}

        added: bool = False
        
        for layer in dag.layers():
            for node in layer['graph'].front_layer():
                if node.name == CXGate().name:
                    c_bit: Qubit = node.qargs[0]
                    o_bit: Qubit = node.qargs[1]
                    c_bit_index: int = self.circuit.find_bit(c_bit).index
                    o_bit_index: int = self.circuit.find_bit(o_bit).index

                    # If cx operations overlap then it is unlikely this pattern.
                    if o_bit_index in cx_nodes.keys() or o_bit_index in cx_nodes.values() \
                        or c_bit_index in cx_nodes.values():
                        
                        cx_nodes.clear()

                    cx_nodes[c_bit_index] = o_bit_index
                    added = True

                if node.name == SwapGate().name:
                    first_bit: Qubit = node.qargs[0]
                    second_bit: Qubit = node.qargs[1]
                    first_bit_index: int = self.circuit.find_bit(first_bit).index
                    second_bit_index: int = self.circuit.find_bit(second_bit).index

                    for key in cx_nodes.copy().keys():
                        if (key == first_bit_index and cx_nodes[key] == second_bit_index) or \
                            key == second_bit_index and cx_nodes[key] == first_bit_index:

                            del cx_nodes[key]

                if added and not cx_nodes:
                    return "Uncompute: Instance of Uncompute detected."


if __name__ == '__main__':
    input_file: TextIOWrapper = open("C:/quantum-pattern-detector/code-example.txt")
    msg: str = UncomputeDetector(input_file).build_message()
    print(msg)
