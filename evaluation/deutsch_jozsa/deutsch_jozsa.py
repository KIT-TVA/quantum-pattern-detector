# Code adapted from https://learn.qiskit.org/course/ch-algorithms/deutsch-jozsa-algorithm

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister

def dj_circle() -> QuantumCircuit:
    
    q = QuantumRegister(3,"q")
    c = ClassicalRegister(3,"c")
    circuit = QuantumCircuit(q,c)

    circuit.h(q[0])
    circuit.h(q[1])
    circuit.barrier(q)
    
    circuit.x(q[2])
    circuit.h(q[2])
    circuit.barrier(q)

    circuit.cx(q[0], q[2])
    circuit.cx(q[1], q[2])
    circuit.barrier(q)

    circuit.h(q[2])
    circuit.x(q[2])
    circuit.barrier(q)

    circuit.h(q[0])
    circuit.h(q[1])
    circuit.barrier(q)
    circuit.measure(q[0], c[0])
    circuit.measure(q[1], c[1])
    circuit.barrier(q)

    return circuit
    