# Code adapted from https://qiskit.org/ecosystem/finance/tutorials/00_amplitude_estimation.html

import numpy as np

from qiskit import QuantumCircuit
from qiskit_algorithms import AmplitudeEstimation, EstimationProblem

from qiskit.qasm2 import dumps


def ae_circuit(num_qubits: int) -> QuantumCircuit:

    # -1 because of the to be estimated qubit
    ae = AmplitudeEstimation(num_eval_qubits=num_qubits - 1)
    problem = get_estimation_problem()

    qc = ae.construct_circuit(problem)
    qc.name = "ae"
    qc.measure_all()

    return qc


class BernoulliA(QuantumCircuit):
    """A circuit representing the Bernoulli A operator."""

    def __init__(self, probability):
        super().__init__(1)  # circuit on 1 qubit

        theta_p = 2 * np.arcsin(np.sqrt(probability))
        self.ry(theta_p, 0)


class BernoulliQ(QuantumCircuit):
    """A circuit representing the Bernoulli Q operator."""

    def __init__(self, probability: float) -> None:
        super().__init__(1)  # circuit on 1 qubit

        self._theta_p = 2 * np.arcsin(np.sqrt(probability))
        self.ry(2 * self._theta_p, 0)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, BernoulliQ) and self._theta_p == other._theta_p

    def power(self, power: float) -> QuantumCircuit:
        # implement the efficient power of Q
        q_k = QuantumCircuit(1)
        q_k.ry(2 * power * self._theta_p, 0)
        return q_k


def get_estimation_problem() -> EstimationProblem:
    
    """Returns a estimation problem instance for a fixed value."""
    to_estimate = 0.2

    return EstimationProblem(
        state_preparation=BernoulliQ(to_estimate),  # A operator
        grover_operator=BernoulliQ(to_estimate),  # Q operator
        objective_qubits=[0],  # the "good" state Psi1 is identified as measuring |1> in qubit 0
    )
