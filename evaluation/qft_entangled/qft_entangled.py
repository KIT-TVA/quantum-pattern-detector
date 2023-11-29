# Code adapted from https://github.com/cda-tum/mqt-bench/blob/main/src/mqt/bench/benchmarks/qftentangled.py

from qiskit import QuantumCircuit, QuantumRegister
from qiskit.circuit.library import QFT


def entangled_qft_circuit(num_qubits: int) -> QuantumCircuit:
    """Returns a quantum circuit implementing the Quantum Fourier Transform algorithm using entangled qubits.

    Keyword arguments:
    num_qubits -- number of qubits of the returned quantum circuit
    """

    q = QuantumRegister(num_qubits, "q")
    qc = QuantumCircuit(q)
    qc.h(q[-1])
    for i in range(1, num_qubits):
        qc.cx(q[num_qubits - i], q[num_qubits - i - 1])

    qc.compose(QFT(num_qubits=num_qubits), inplace=True)

    qc.measure_all()
    qc.name = "qftentangled"

    return qc