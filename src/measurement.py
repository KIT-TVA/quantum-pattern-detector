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

    def build_message(self) -> str:
        found: bool = False
        message: str = ""
        dag: DAGCircuit = circuit_to_dag(self.circuit)

        # key: Target register for measurement
        # value: Index of qubit to measure
        measurements: dict = {}

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
                            message += "Post Selective Measurement: Post Selective Measurement "\
                                       "performed on qubit {index}.\n".format(index=measurements[register_name])
                            del measurements[register_name]

        if not found: 
            message = "Post Selective Measurement: No instance detected."

        return message.strip()
