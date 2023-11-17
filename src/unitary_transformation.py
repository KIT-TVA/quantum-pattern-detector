from abstract_detector import PatternDetector

from qiskit.circuit.quantumcircuit import BitLocations, Qubit
from qiskit.converters import circuit_to_dag
from qiskit.dagcircuit import DAGCircuit
from qiskit.circuit.library import HGate, CXGate, SwapGate
from io import TextIOWrapper

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
                
        return "Quantum Phase Estimation: No instance detected."


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

        return "Uncompute: No instance detected."