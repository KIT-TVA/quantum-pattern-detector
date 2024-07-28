"""Detectors for patterns for the manipulation of quantum states."""

from typing import Any
from utils import FileReader, get_combinations, convert_to_int
from abstract_detector import PatternDetector

from qiskit import Aer, transpile
from qiskit_aer.backends import AerSimulator, StatevectorSimulator
from qiskit_aer.backends.compatibility import Statevector
from qiskit.circuit.library import Measure
from qiskit.converters import circuit_to_dag
from qiskit.dagcircuit import DAGCircuit
from qiskit.quantum_info import schmidt_decomposition
from qiskit.result import Result
from copy import deepcopy
from io import TextIOWrapper


class EntanglementDetector(PatternDetector):
    """Detector for the pattern Creating Entanglement."""

    def __init__(self, program: TextIOWrapper) -> None:
        """Create a new detector for Creating Entanglement.
        
        Args:
            program (TextIOWrapper): Wrapper that encodes the OPENQASM file in which patterns should be detected.
        """
        super().__init__(program)

    def detect_pattern(self) -> list[tuple[int, int]]:
        """Detect instances of Creating Entanglement.

        Creating Entanglement refers to the process of creating a strong correlation between qubits.
        The pattern is detected by analyzing the Schmidt decomposition of the quantum states.
        
        Returns:
            list[tuple[int, int]]: A list of tuples consisting of start and end line of the given OPENQASM code where
                                   the quantum state is entangled.
        """
        pattern_instances: list[tuple[int, int]] = []
        current_start_line: int = -1
        is_entangled: bool = True
        reader: FileReader = FileReader(self.program)
        program_len: int = len(self.program.readlines())
        self.program.seek(0)

        # Read input file line after line.
        for line_num in range(0, program_len):
            current_program: str = reader.read_file_until(line_num)
            self.load_circuit_from_str(current_program)

            if self.circuit.depth() == 0:
                if is_entangled:
                    is_entangled = False
                continue

            # Calculate the state vector of the circuit.
            backend: StatevectorSimulator = Aer.get_backend('statevector_simulator')
            self.circuit = transpile(self.circuit, backend)
            result: Result = backend.run(self.circuit).result()
            outputstate: Statevector = result.get_statevector(self.circuit)

            # Determines if a quantum state is entangled using Schmidt decomposition.
            combinations: list[list[int]] = list(get_combinations(range(0, self.circuit.num_qubits)))[1:-1]
            found: bool = False
            for comb in combinations:
                decomp: list[tuple[Any, Statevector, Statevector]] = schmidt_decomposition(outputstate, comb)

                schmidt_coefficents: list[float] = []
                for decomp_elem in decomp:
                    schmidt_coefficents.append(decomp_elem[0])

                # Number of posititve Schmidt coefficients is called the Schmidt-rank of the state vector.
                # The quantum state is entangled iff the Schmidt-rank is greater than 1.
                if len(schmidt_coefficents) > 1:
                    if not is_entangled:
                        current_start_line = line_num + 1
                        is_entangled = True
                    found = True
                    break

            if found:
                found = False
                continue

            if is_entangled:
                pattern_instances.append((current_start_line, line_num))
                current_start_line = -1
                is_entangled = False
                
        if current_start_line != -1:
            pattern_instances.append((current_start_line, program_len))

        return pattern_instances

    def build_message(self) -> str:
        """Construct a human-readable message about the detection result.
        
        Returns:
            str: Message that contains code places where the pattern was detected.
        """
        message: str = ""

        for instance in self.detect_pattern():
            message += ("Creating Entanglement: Quantum state is entangled "
                        "from line {start_ln} to {end_ln}.\n".format(start_ln=instance[0], end_ln=instance[1]))
            
        return message


class UniformSuperpositionDetector(PatternDetector):
    """Detector for the pattern Uniform Superposition."""

    def __init__(self, program: TextIOWrapper) -> None:
        """Create a new detector for Uniform Superposition.
        
        Args:
            program (TextIOWrapper): Wrapper that encodes the OPENQASM file in which patterns should be detected.
        """
        super().__init__(program)
        self.load_circuit(self.program)

    def detect_pattern(self) -> list[tuple[int, int]]:
        """Detect instances of Uniform Superposition.

        A quantum state is in Uniform Superposition if all possible outcomes of the quantum register are equally likely.
        The pattern is detected by analysing the state probabilities.
        
        Returns:
            list[tuple[int, int]]: A list of tuples consisting of start and end line of the given OPENQASM code where
                                   the quantum state is in Uniform Superposition.
        """
        pattern_instances: list[tuple[int, int]] = []
        current_start_line: int = -1
        in_ufs: bool = True
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
                    in_ufs = False
                continue

            # Probabilities can somehow vary if measurements occur.
            has_measurement: bool = False
            reversed_dag: DAGCircuit = circuit_to_dag(self.circuit).reverse_ops()
            for node in reversed_dag.front_layer():
                if node.name == Measure().name:
                    has_measurement = True
            
            prob: list[float] = [0] * (2 ** self.circuit.num_qubits)

            # Calculate measurement probabilities by simulating measurements.
            if has_measurement:
                backend: AerSimulator = Aer.get_backend('aer_simulator')
                self.circuit = transpile(self.circuit, backend)
                result: Result = backend.run(self.circuit).result()
                counts: dict[str, int] = result.get_counts()
                shots: int = sum(counts.values())

                for key, value in counts.items():
                    state: str = key.replace(" ", "")
                    prob[int(state, 2)] = value / shots

                has_measurement = False

            else: 
                # Calculate probabilities by analysing the statevector.
                backend: StatevectorSimulator = Aer.get_backend('statevector_simulator')
                self.circuit = transpile(self.circuit, backend)
                result: Result = backend.run(self.circuit).result()
                outputstate: Statevector = result.get_statevector(self.circuit)
                prob = outputstate.probabilities()
            
            # Round probabilities for better comparison.
            rounded_prob: list[float] =  [round(x,4) for x in prob] 

            # Binary encodes states
            binary_combinations: list[str] = self.calc_all_binary_combinations(self.circuit.num_qubits)

            # All possible ancilla bits
            state_combinations: list[list[int]] = list(get_combinations(range(0, self.circuit.num_qubits)))
            state_combinations.pop()

            found: bool = False
            for state in state_combinations:
                c_binary_combinations: list[str] = deepcopy(binary_combinations)

                filtered_states_0: list[str] = self.filter_indices(c_binary_combinations, state, '0')
                filtered_states_1: list[str] = self.filter_indices(c_binary_combinations, state, '1')

                if self.in_ufs(rounded_prob, convert_to_int(filtered_states_0)) or \
                    self.in_ufs(rounded_prob, convert_to_int(filtered_states_1)):

                    if not in_ufs:
                        current_start_line = line_num + 1
                        in_ufs = True

                    found = True
                    break

            if found:
                found = False
                continue

            if in_ufs:
                in_ufs = False
                pattern_instances.append((current_start_line, line_num))
                current_start_line = -1
        
        if current_start_line != -1:
            pattern_instances.append((current_start_line, program_len))

        return pattern_instances

    def build_message(self) -> str:
        """Construct a human-readable message about the detection result.
        
        Returns:
            str: Message that contains code places where the pattern was detected.
        """
        message: str = ""

        for instance in self.detect_pattern():
            message += ("Uniform Superposition: Quantum system is in uniform superposition "
                        "from line {start_ln} to {end_ln}.\n".format(start_ln=instance[0], end_ln=instance[1]))
            
        return message

    @staticmethod
    def calc_all_binary_combinations(n: int) -> list[str]:
        """Calculate all binary numbers up to a given decimal number.

        This method is used for converting quantum states into binary representation for further processing.
        
        Args:
            n (int): The upper bound in decimal representation to which binary numbers should be generated.

        Returns:
            list[str]: List containing the generated binary numbers.
        """
        result: list[str] = []
        for i in range(1 << n):
            # Convert the current number to a binary string of length n
            binary_str: str = format(i, '0' + str(n) + 'b')
            result.append(binary_str)

        return result

    @staticmethod
    def filter_indices(binary_list: list[str], index_list: list[int], significant_bit: str) -> list[str]:
        """Filter a given list of binary strings by comparing bits on certain indices with a significant bit.

        This method is used for considering the usage of ancilla bits. If ancilla bits are used, then the probabilities 
        of only a part of all quantum states have to be taken into account for detecting Uniform Superposition.
        
        Args:
            binary_list (list[str]): List of strings which represent binary numbers.
            index_list (list[int]): List of indices of bits that are compared with the significant bit.
            significant_bit (str): Bit to which bits of the binary string are compared to. It is used for filtering.
        """
        list_copy: list[str] = deepcopy(binary_list)
        to_delete: list[str] = []
        elem_count: int = 0
        for i in range(0, len(binary_list)):
            for index in index_list:
                if binary_list[i][index] != significant_bit:
                    to_delete.append(i-elem_count)
                    elem_count += 1
                    break

        for i in to_delete:
            list_copy.pop(i)

        return list_copy

    @staticmethod
    def in_ufs(list: list[float], indices: list[int]) -> bool:
        """Checks if all values in a list on certain indices are the same.
        
        This method is used for verifying if a quantum state is in Uniform Superposition by comparing if all state
        probabilities are the same.

        Args:
            list (list[float]): The input list with state probabilities.
            indices (list[float]): List of indices that have to be taken into consideration. This is needed due to the
                                   fact of ancilla bits. In that case not all state probabilities are relevant.
        """
        to_compare: float = list[indices[0]]

        if to_compare == 0:
            return False

        for i in indices:
            if list[i] != to_compare:
                return False

        total: float = 0.0
        for i in indices:
            total += list[i]

        if total != 1:
            return False

        return True
