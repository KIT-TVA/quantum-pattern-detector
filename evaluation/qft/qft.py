# Code adapted from https://github.com/cda-tum/mqt-bench/blob/main/src/mqt/bench/benchmarks/qft.py

from qiskit import QuantumCircuit, QuantumRegister
from qiskit.circuit.library import QFT

import qiskit.qasm2


def qft_circuit(num_qubits: int) -> QuantumCircuit:
    """Returns a quantum circuit implementing the Quantum Fourier Transform algorithm.

    Keyword arguments:
    num_qubits -- number of qubits of the returned quantum circuit
    """

    q = QuantumRegister(num_qubits, "q")
    qc = QuantumCircuit(q, name="qft")
    qc.compose(QFT(num_qubits=num_qubits), inplace=True)
    qc.measure_all()

    return qc