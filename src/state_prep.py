from abstract_detector import PatternDetector

from qiskit import QuantumRegister
from qiskit.circuit.library import XGate, RYGate
from qiskit.circuit.quantumcircuit import BitLocations, Qubit
from qiskit.converters import circuit_to_dag
from qiskit.dagcircuit import DAGCircuit
from math import pi
from io import TextIOWrapper


class AngleEncodingDetector(PatternDetector):

    THRESHOLD: float = 0.3

    def __init__(self, program: TextIOWrapper) -> None:
        super().__init__(program)
        self.load_circuit(self.program)

    # Search for R_y gates in the first layer.
    def build_message(self) -> str:
        message: str = ""
        gate_count: int = 0
        dag: DAGCircuit = circuit_to_dag(self.circuit)

        for node in dag.front_layer():
            # Angle has to satisfy normalization constraint.
            if node.name == RYGate(0).name and node.op.params[0] < pi:
                gate_count += 1
                qubit: Qubit = node.qargs[0]
                location: BitLocations = self.circuit.find_bit(qubit)
                register: QuantumRegister = location.registers[0][0]
                message += "Angle Encoding: Qubit {qubit} in quantum register {reg} is used for angle encoding.\n"\
                    .format(qubit=location.index, reg=register.name)
        
        if gate_count < self.THRESHOLD * self.circuit.num_qubits:
            message = ""

        return message.strip()


class AmplitudeEncodingDetector(PatternDetector):
    
    # There are many methods for creating amplitude encoding which makes it difficult to detect.
    pass


class BasisEncodingDetector(PatternDetector):

    THRESHOLD: float = 0.5
    
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

        for register in encoded_nums.copy().keys():
            if len(encoded_nums[register]) < self.THRESHOLD * register.size:
                del encoded_nums[register]

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

        binary_list.reverse()
        
        return sum(val*(2**idx) for idx, val in enumerate(binary_list))
