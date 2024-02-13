"""Detectors for patterns for state preparation."""

from abstract_detector import PatternDetector

from qiskit import QuantumRegister, QuantumCircuit
from qiskit.circuit.library import XGate, RYGate, CXGate
from qiskit.circuit.quantumcircuit import BitLocations, Qubit
from qiskit.converters import circuit_to_dag
from qiskit.dagcircuit import DAGCircuit

from io import TextIOWrapper


class AngleEncodingDetector(PatternDetector):
    """Detector for the pattern Angle Encoding."""

    THRESHOLD: float = 0.3

    def __init__(self, program: TextIOWrapper) -> None:
        """Create a new detector for Angle Encoding.
        
        Args:
            program (TextIOWrapper): Wrapper that encodes the OPENQASM file in which patterns should be detected.
        """
        super().__init__(program)
        self.load_circuit(self.program)

    def detect_pattern(self) -> list[tuple[int, str]]:
        """Detect instances of Angle Encoding.

        Angle Encoding refers to the process of encoding classical data by rotating qubits. The pattern is detected by
        searching for rotation gates in the first layer of the quantum circuit.

        Returns:
            list[tuple[int, str]]: List of tuples containing the index of the rotated qubit and the name of the 
                                   quantum register to which it corresponds to.
        """
        instances: list[tuple[int, str]] = find_gates_in_first_layer(RYGate(0).name, self.circuit)
            
        if len(instances) < self.THRESHOLD * self.circuit.num_qubits:
            return []
            
        return instances

    def build_message(self) -> str:
        """Construct a human-readable message about the detection result.
        
        Returns:
            str: Message that contains the indices and registers of qubits that are used for Angle Encoding.
        """
        message = ""
        instances: list[tuple[int, str]] = self.detect_pattern()

        if not instances:
            return "Angle Encoding: No instance found.\n"
        
        message = "Angle Encoding: Instance of Angle Encoding detected.\n"

        for instance in instances:
            message += ("Angle Encoding: Qubit {q} of register {r} "
                        "is used for Basis Encoding.\n".format(q=instance[0], r=instance[1]))
            
        return message


class AmplitudeEncodingDetector(PatternDetector):

    THRESHOLD: int = 2
    
    def __init__(self, program: TextIOWrapper) -> None:
        """Create a new detector for Amplitude Encoding.
        
        Args:
            program (TextIOWrapper): Wrapper that encodes the OPENQASM file in which patterns should be detected.
        """
        super().__init__(program)
        self.load_circuit(self.program)
    
    def detect_pattern(self) -> bool:
        """Detect instances of Amplitude Encoding.

        Amplitude Encoding refers to the process of encoding classical data into the amlitudes of qubits.
        There are several methods for implementing this idea. Our detection method is only capable of recognizing 
        the implementation provided in [1] which also used in Qiskit.

        **References:**
        [1] Shende, Bullock, Markov. Synthesis of Quantum Logic Circuits (2004)
        [`https://arxiv.org/abs/quant-ph/0406176v5`]

        Returns:
            bool: True if an instance of Amplitude Encoding was detected, False otherwise.
        """
        dag: DAGCircuit = circuit_to_dag(self.circuit)
        structure_count: int = 0
        rotation_layer_found: bool = False
        expecting_layer_found: bool = False

        possible_rotation_gates: list[str] = ["u3", "u2", "u1", "u", "rx", "ry", "rz",]

        for layer in dag.layers():
            for node in layer['graph'].front_layer():
                if node.name in possible_rotation_gates and not rotation_layer_found:
                    rotation_layer_found = True
                    expecting_layer_found = True
                    break

                if rotation_layer_found and node.name == CXGate().name:
                    structure_count += 1
                    rotation_layer_found = False
                    expecting_layer_found = True
                    break

            if structure_count >= self.THRESHOLD:
                return True
            
            if not expecting_layer_found:
                structure_count = 0
                rotation_layer_found = False
            
            expecting_layer_found = False
        
        return False
    
    def build_message(self) -> str:
        """Construct a human-readable message about the detection result.
        
        Returns:
            str: Message with information whether an instance of Amlitude Encoding was detected.
        """
        if self.detect_pattern():
            return "Amlitude Encoding: Instance of Amlpitude Encoding detected.\n"

        return "Amlitude Encoding: No instance detected.\n"


class BasisEncodingDetector(PatternDetector):
    """Detector for the pattern Basis Encoding."""

    THRESHOLD: float = 0.3
    
    def __init__(self, program: TextIOWrapper) -> None:
        """Create a new detector for Basis Encoding.
        
        Args:
            program (TextIOWrapper): Wrapper that encodes the OPENQASM file in which patterns should be detected.
        """
        super().__init__(program)
        self.load_circuit(self.program)

    def detect_pattern(self) -> list[tuple[int, str]]:
        """Detect instances of Basis Encoding.

        Basis Encoding refers to the process of encoding classical data by applying Pauli-X gates on the qubits.
        The pattern is therefore detected by searching for Pauli-X gates in the first layer of the quantum circuit.

        Returns:
            list[tuple[int, str]]: List of tuples containing the index and the register name of the qubits which are 
                                   used for Basis Encoding.
        """
        instances: list[tuple[int, str]] = find_gates_in_first_layer(XGate().name, self.circuit)
            
        if len(instances) < self.THRESHOLD * self.circuit.num_qubits:
            return []
            
        return instances

    def build_message(self) -> str:
        """Construct a human-readable message about the detection result.
        
        Returns:
            str: Message that contains the indices and registers of qubits that are used for Basis Encoding.
        """
        message = ""
        instances: list[tuple[int, str]] = self.detect_pattern()

        if not instances:
            return "Basis Encoding: No instance found.\n"
        
        message = "Basis Encoding: Instance of Basis Encoding detected.\n"

        for instance in instances:
            message += ("Basis Encoding: Qubit {q} of register {r} "
                        "is used for Basis Encoding.\n".format(q=instance[0], r=instance[1]))
            
        return message


def find_gates_in_first_layer(gate_name: str, circuit: QuantumCircuit) -> list[tuple[int, str]]:
    """Find a certain quantum gate in the first layer of a quantum circuit.
    
    Args:
        gate_name (str): Gate name of the quantum gate to search for.
        circuit (QuantumCircuit): Quantum circuit in which the gate is searched.
    
    Returns:
        list[tuple[int, str]]: List of tuples containing the indices and registers of qubits to which the gate is
                               is applied to.
    """
    instances: list[tuple[int, str]] = []
    dag: DAGCircuit = circuit_to_dag(circuit)

    for node in dag.front_layer():
        if node.name == gate_name:
            qubit: Qubit = node.qargs[0]
            location: BitLocations = circuit.find_bit(qubit)
            register: QuantumRegister = location.registers[0][0]

            instances.append((location.index, register.name))

    return instances