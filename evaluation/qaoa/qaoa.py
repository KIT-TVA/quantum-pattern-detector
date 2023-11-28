# Code adapted from https://github.com/qiskit-community/qiskit-application-modules-demo-sessions/blob/main/qiskit-optimization/qiskit-optimization-demo.ipynb

import networkx as nx

from qiskit import QuantumCircuit
from qiskit_algorithms import QAOA
from qiskit_algorithms.optimizers import SLSQP
from qiskit.primitives import Sampler
from qiskit_optimization import QuadraticProgram  
from qiskit_optimization.applications import Maxcut 


def qaoa_circuit(num_qubits: int) -> QuantumCircuit:
    """Returns a quantum circuit implementing the Quantum Approximation Optimization Algorithm for a specific max-cut
     example.

    Keyword arguments:
    num_qubits -- number of qubits of the returned quantum circuit
    """

    graph = nx.random_regular_graph(2, num_qubits, seed=111)
    maxcut = Maxcut(graph)
    qp = maxcut.to_quadratic_program()
    assert isinstance(qp, QuadraticProgram)

    qaoa = QAOA(sampler=Sampler(), reps=2, optimizer=SLSQP(maxiter=25))
    qaoa_result = qaoa.compute_minimum_eigenvalue(qp.to_ising()[0])
    qc = qaoa.ansatz.assign_parameters(qaoa_result.optimal_point)

    qc.name = "qaoa"

    return qc