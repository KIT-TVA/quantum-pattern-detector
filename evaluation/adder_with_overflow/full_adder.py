from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister


def adder_circuit(a_flag = False, b_flag = False, c_in = False) -> QuantumCircuit:
    q = QuantumRegister(5,'q')
    c = ClassicalRegister(2,'c')
    circuit = QuantumCircuit(q,c)

    if a_flag:
        circuit.x(q[0])

    if b_flag:
        circuit.x(q[1])

    if c_in:
        circuit.x(q[2])

    circuit.cx(q[0],q[3])
    circuit.cx(q[1],q[3])
    circuit.cx(q[2],q[3])
    circuit.ccx(q[0],q[1],q[4])
    circuit.ccx(q[0],q[2],q[4])
    circuit.ccx(q[1],q[2],q[4])

    circuit.measure(q[3],c[0])
    circuit.measure(q[4],c[1])

    return circuit
