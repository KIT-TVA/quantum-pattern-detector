from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit.library import RGQFTMultiplier


def multiplier_circuit():
    q = QuantumRegister(8,'q')
    c = ClassicalRegister(4,'c')

    circuit = QuantumCircuit(q,c)

    # Operand A = 10 (2)
    circuit.x(q[1])

    # Operand B = 11 (3)
    circuit.x(q[2])
    circuit.x(q[3])

    mult_circuit = RGQFTMultiplier(num_state_qubits=2, num_result_qubits=4)
    circuit = circuit.compose(mult_circuit)

    circuit.measure(q[4],c[0])
    circuit.measure(q[5],c[1])
    circuit.measure(q[6],c[2])
    circuit.measure(q[7],c[3])

    return circuit