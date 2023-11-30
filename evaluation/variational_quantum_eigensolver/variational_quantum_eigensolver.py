# Code adapted from https://github.com/cda-tum/mqt-bench/blob/main/src/mqt/bench/benchmarks/vqe.py

import networkx as nx

from qiskit import QuantumCircuit
from qiskit_algorithms.minimum_eigensolvers import VQE
from qiskit_algorithms.optimizers import SLSQP
from qiskit.circuit.library import RealAmplitudes
from qiskit.primitives import Estimator
from qiskit_optimization import QuadraticProgram
from qiskit_optimization.applications import Maxcut


def vqe_circuit(num_qubits: int) -> QuantumCircuit:
    """Returns a quantum circuit implementing the Variational Quantum Eigensolver Algorithm for a specific max-cut
     example.

    Keyword arguments:
    num_qubits -- number of qubits of the returned quantum circuit
    """
    graph = nx.random_regular_graph(2, num_qubits, seed=111)
    maxcut = Maxcut(graph)

    qp = maxcut.to_quadratic_program()
    assert isinstance(qp, QuadraticProgram)

    ansatz = RealAmplitudes(num_qubits, reps=2)
    vqe = VQE(ansatz=ansatz, optimizer=SLSQP(maxiter=25), estimator=Estimator())
    vqe_result = vqe.compute_minimum_eigenvalue(qp.to_ising()[0])
    qc = vqe.ansatz.assign_parameters(vqe_result.optimal_point)

    qc.measure_all()
    qc.name = "vqe"

    return qc