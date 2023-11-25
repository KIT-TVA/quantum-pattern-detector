from utils import FileReader, get_combinations, convert_to_int
from abstract_detector import PatternDetector

from qiskit import Aer, transpile
from qiskit_aer.backends import StatevectorSimulator
from qiskit_aer.backends.compatibility import Statevector
from qiskit.quantum_info import schmidt_decomposition
from qiskit.result import Result
from copy import deepcopy
from io import TextIOWrapper


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
            self.load_circuit_from_str(current_program)

            if self.circuit.depth() == 0:
                if is_entangled:
                    message += "Creating Entanglement: Quantum state is not entangled from line {ln} onwards.\n"\
                        .format(ln=line_num + 1)
                    is_entangled = False
                continue

            # Calculate the state vector of the circuit.
            backend: StatevectorSimulator = Aer.get_backend('statevector_simulator')
            self.circuit = transpile(self.circuit, backend)
            result: Result = backend.run(self.circuit).result()
            outputstate: Statevector = result.get_statevector(self.circuit)

            # Determines if a quantum state is entangled using Schmidt decomposition.
            combinations: list = list(get_combinations(range(0, self.circuit.num_qubits)))[1:-1]
            found: bool = False
            for comb in combinations:
                decomp: list = schmidt_decomposition(outputstate, comb)

                schmidt_coefficents: list = []
                for decomp_elem in decomp:
                    schmidt_coefficents.append(decomp_elem[0])

                # Number of posititve Schmidt coefficients is called the Schmidt-rank of the state vector.
                # The quantum state is entangled iff the Schmidt-rank is greater than 1.
                if len(schmidt_coefficents) > 1:
                    if not is_entangled:
                        message += "Creating Entanglement: Quantum state is entangled from line {ln} onwards.\n"\
                            .format(ln=line_num + 1)
                        is_entangled = True
                    found = True
                    break

            if found:
                found = False
                continue

            if is_entangled:
                is_entangled = False
                message += "Creating Entanglement: Quantum state is not entangled from line {ln} onwards.\n"\
                    .format(ln=line_num + 1)

        return message.strip()

    
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
            self.load_circuit_from_str(current_program)

            # Circuit with depth of 0 cannot be in uniform superposition.
            if self.circuit.depth() == 0:
                if in_ufs:
                    message += ("Uniform Superposition: Quantum state is not in uniform superposition"
                                "from line {ln} onwards.\n").format(ln=line_num + 1)
                    in_ufs = False
                continue

            # Calculate the state vector of the circuit.
            backend: StatevectorSimulator = Aer.get_backend('statevector_simulator')
            self.circuit = transpile(self.circuit, backend)
            result: Result = backend.run(self.circuit).result()
            outputstate: Statevector = result.get_statevector(self.circuit)

            # Calculate state probabilities and check if they are all equal. Ancilla bits, that do not have to be in
            # superposition, are also taken into account.
            prob: list = outputstate.probabilities()
            rounded_prob: list =  [round(x,3) for x in prob] 

            # Binary encodes states
            binary_combinations: list = self._calc_all_binary_combinations(self.circuit.num_qubits)

            # All possible ancilla bits
            state_combinations: list = list(get_combinations(range(0, self.circuit.num_qubits)))
            state_combinations.pop()

            found: bool = False
            for state in state_combinations:
                c_binary_combinations: list = deepcopy(binary_combinations)
                filtered_states: list = self._filter_indices(c_binary_combinations, state)

                if self._in_ufs(rounded_prob, convert_to_int(filtered_states)):
                    if not in_ufs:
                        message += ("Uniform Superposition: Quantum state is in uniform superposition"
                                    "from line {ln} onwards.\n").format(ln=line_num + 1)
                        in_ufs = True

                    found = True
                    break

            if found:
                found = False
                continue

            if in_ufs:
                in_ufs = False
                message += ("Uniform Superposition: Quantum state is not in uniform superposition"
                            "from line {ln} onwards.\n").format(ln=line_num + 1)

        return message.strip()

    def _calc_all_binary_combinations(self, n: int) -> list:
        result: list = []
        for i in range(1 << n):
            # Convert the current number to a binary string of length n
            binary_str = format(i, '0' + str(n) + 'b')
            result.append(binary_str)

        return result

    def _filter_indices(self, binary_list: list, index_list: list) -> list:
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

    def _in_ufs(self, list: list, indices: list) -> bool:
        to_compare = list[indices[0]]

        if to_compare == 0:
            return False

        for i in indices:
            if list[i] != to_compare:
                return False

        total: int = 0 
        for i in indices:
            total += list[i]

        if total != 1:
            return False

        return True
