import qiskit.qasm2

from abc import ABC, abstractmethod
from io import TextIOWrapper
from qiskit import QuantumCircuit

class PatternDetector(ABC):

    def __init__(self, program: TextIOWrapper) -> None:
        self.program: TextIOWrapper = program
        self.circuit: QuantumCircuit = None

    def load_circuit(self, program: TextIOWrapper) -> None:
        program_str: str = program.read()
        self.program.seek(0) 
        self.load_circuit_from_str(program_str)

    def load_circuit_from_str(self, program_str: str) -> None:

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