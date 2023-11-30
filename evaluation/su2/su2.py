# Code adapted from https://github.com/cda-tum/mqt-bench/blob/main/src/mqt/bench/benchmarks/su2random.py

import numpy as np

from qiskit.circuit.library import EfficientSU2
from qiskit import QuantumCircuit


def su2_circuit(num_qubits: int) -> QuantumCircuit:
    """Returns a quantum circuit implementing EfficientSU2 ansatz with random parameter
    values.

    Keyword arguments:
    num_qubits -- number of qubits of the returned quantum circuit
    """

    np.random.seed(10)
    qc = EfficientSU2(num_qubits, entanglement="full", reps=2)
    num_params = qc.num_parameters
    qc = qc.bind_parameters(2 * np.pi * np.random.rand(num_params))
    qc.measure_all()
    qc.name = "su2random"

    return qc