from typing import Any
from abstract_detector import PatternDetector

from qiskit.circuit.library import Measure
from qiskit.circuit.quantumcircuit import BitLocations, Qubit
from qiskit.converters import circuit_to_dag
from qiskit.dagcircuit import DAGCircuit
from io import TextIOWrapper


class PostSelectiveMeasurementDetector(PatternDetector):

    def __init__(self, program: TextIOWrapper) -> None:
        super().__init__(program)
        self.load_circuit(self.program)

    def detect_pattern(self) -> list[int]:
        found: bool = False
        instances: list[int] = []
        dag: DAGCircuit = circuit_to_dag(self.circuit)

        # key: Target register for measurement
        # value: Index of qubit to measure
        measurements: dict[str, int] = {}

        for layer in dag.layers():
            for node in layer['graph'].front_layer():
                if node.name == Measure().name:
                    qubit: Qubit = node.qargs[0]
                    location: BitLocations = self.circuit.find_bit(qubit)
                    qubit_index: int = location.index
                    register_name: str = node.cargs[0].register.name

                    measurements[register_name] = qubit_index
                
                if len(node.op.condition_bits) != 0:
                    for clbit in node.op.condition_bits:
                        register_name: str = clbit.register.name

                        if register_name in measurements.keys():
                            found = True
                            instances.append(measurements[register_name])
                            del measurements[register_name]

        if not found: 
            return []

        return instances


    def build_message(self) -> str:
        message = ""
        instances: list[int] = self.detect_pattern()

        if not instances:
            return "Post Selective Measurement: No instance found.\n"
        
        message = "Post Selective Measurement: Instance of Post Selective Measurement detected.\n"

        for instance in instances:
            message += ("Post Selective Measurement: Post Selective Measurement "\
                        "performed on qubit {index}.\n".format(index=instance))
            
        return message