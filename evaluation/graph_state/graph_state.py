# Code adapted from https://github.com/cda-tum/mqt-bench/blob/main/src/mqt/bench/benchmarks/graphstate.py

import networkx as nx
from qiskit import QuantumCircuit, QuantumRegister
from qiskit.circuit.library import GraphState

import qiskit.qasm2


def graph_state_circuit(num_qubits: int, degree: int = 2) -> QuantumCircuit:
    """Returns a quantum circuit implementing a graph state.

    Keyword arguments:
    num_qubits -- number of qubits of the returned quantum circuit
    degree -- number of edges per node
    """

    q = QuantumRegister(num_qubits, "q")
    qc = QuantumCircuit(q, name="graphstate")

    g = nx.random_regular_graph(degree, num_qubits)
    a = nx.convert_matrix.to_numpy_array(g)
    qc.compose(GraphState(a), inplace=True)
    qc.measure_all()

    return qc
