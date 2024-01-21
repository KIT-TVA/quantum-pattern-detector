"""Abstract detector for quantum computing patterns."""

import qiskit.qasm2
import qiskit.qasm3

from abc import ABC, abstractmethod
from io import TextIOWrapper
from typing import Any
from qiskit import QuantumCircuit

class PatternDetector(ABC):
    """Implement an abstract quantum pattern detector."""

    def __init__(self, program: TextIOWrapper, mode: int=2) -> None:
        """Create a new quantum pattern detector.
        
        Args:
            program (TextIOWrapper): Wrapper that encodes the OPENQASM file in which patterns should be detected.
            mode (int): OpenQASM version of the input code.
        """

        self.program: TextIOWrapper = program
        self.circuit: QuantumCircuit = None
        self.mode: int = mode

    def load_circuit(self, program: TextIOWrapper) -> None:
        """Load a given OPENQASM program as a quantum circuit.
        
        Args:
            program (TextIOWrapper): Wrapper that encodes the OPENQASM file which sould be loaded.
        """
        program_str: str = program.read()
        self.program.seek(0) 
        self.load_circuit_from_str(program_str)

    def load_circuit_from_str(self, program_str: str) -> None:
        """Load a quantum circuit from a given OPENQASM string.
        
        Args:
            program_str (str): The string of the OPENQASM program that should be loaded.

        Raise:
            ValueError: If the given OpenQASM version is not supported.
        """
        
        if self.mode == 2:
            # Workaround to find all possible gates due to a bug in qiskit's current parser.
            self.circuit: QuantumCircuit = qiskit.qasm2.loads(
                program_str, 
                include_path=qiskit.qasm2.LEGACY_INCLUDE_PATH,
                custom_instructions=qiskit.qasm2.LEGACY_CUSTOM_INSTRUCTIONS,
                custom_classical=qiskit.qasm2.LEGACY_CUSTOM_CLASSICAL
            )

        elif self.mode == 3:
            self.circuit: QuantumCircuit = qiskit.qasm3.loads(program_str)

        else:
            raise ValueError("The given OpenQASM version is not supported.")

    @abstractmethod
    def detect_pattern(self) -> Any:
        """Abstract method for detecting a quantum computing pattern.
        
        Returns:
            Any: Object or datatype which describes the detected instance of the quantum pattern.
        """
        pass

    @abstractmethod
    def build_message(self) -> str:
        """Abstract method for construct a human-readable message about the detection result.
        
        Returns:
            str: The message with information about the result of the detection.
        """
        pass
