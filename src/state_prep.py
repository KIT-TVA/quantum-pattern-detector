from typing import Any
from abstract_detector import PatternDetector

from qiskit import QuantumRegister, QuantumCircuit
from qiskit.circuit.library import XGate, RYGate
from qiskit.circuit.quantumcircuit import BitLocations, Qubit
from qiskit.converters import circuit_to_dag
from qiskit.dagcircuit import DAGCircuit
from io import TextIOWrapper


class AngleEncodingDetector(PatternDetector):

    THRESHOLD: float = 0.3

    def __init__(self, program: TextIOWrapper) -> None:
        super().__init__(program)
        self.load_circuit(self.program)

    def detect_pattern(self) -> list[(int, str)]:
        instances: list[(int, str)] = find_gates_in_first_layer(RYGate(0).name, self.circuit)
            
        if len(instances) < self.THRESHOLD * self.circuit.num_qubits:
            return []
            
        return instances

    # Search for R_y gates in the first layer.
    def build_message(self) -> str:
        message = ""
        instances: list[(int, str)] = self.detect_pattern()

        if not instances:
            return "Angle Encoding: No instance found.\n"
        
        message = "Angle Encoding: Instance of Angle Encoding detected.\n"

        for instance in instances:
            message += ("Angle Encoding: Qubit {q} of register {r} "
                        "is used for Basis Encoding.\n".format(q=instance[0], r=instance[1]))
            
        return message


class AmplitudeEncodingDetector(PatternDetector):
    
    # There are many methods for creating amplitude encoding which makes it difficult to detect.
    pass


class BasisEncodingDetector(PatternDetector):

    THRESHOLD: float = 0.3
    
    def __init__(self, program: TextIOWrapper) -> None:
        super().__init__(program)
        self.load_circuit(self.program)

    # Search for Pauli-X gates in the first layer.
    def detect_pattern(self) -> list[(int, str)]:
        instances: list[(int, str)] = find_gates_in_first_layer(XGate().name, self.circuit)
            
        if len(instances) < self.THRESHOLD * self.circuit.num_qubits:
            return []
            
        return instances


    def build_message(self) -> str:
        message = ""
        instances: list[(int, str)] = self.detect_pattern()

        if not instances:
            return "Basis Encoding: No instance found.\n"
        
        message = "Basis Encoding: Instance of Basis Encoding detected.\n"

        for instance in instances:
            message += ("Basis Encoding: Qubit {q} of register {r} "
                        "is used for Basis Encoding.\n".format(q=instance[0], r=instance[1]))
            
        return message


def find_gates_in_first_layer(gate_name: str, circuit: QuantumCircuit) -> list[(int, str)]:
    instances: list[(int, str)] = []
    dag: DAGCircuit = circuit_to_dag(circuit)

    for node in dag.front_layer():
        if node.name == gate_name:
            qubit: Qubit = node.qargs[0]
            location: BitLocations = circuit.find_bit(qubit)
            register: QuantumRegister = location.registers[0][0]

            instances.append((location.index, register.name))

    return instances
