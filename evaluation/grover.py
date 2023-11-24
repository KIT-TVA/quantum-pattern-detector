import math
from qiskit import QuantumCircuit, Aer
from qiskit.circuit.library import GroverOperator, MCMT, ZGate
from qiskit import transpile


# Builds grover circuit for multiple marked states.
def grover_circuit(marked_states: list) -> QuantumCircuit:

    # Compute the number of qubits in circuit.
    num_qubits = len(marked_states[0])

    # Compute oracle for marked states.
    oracle = QuantumCircuit(num_qubits)

    for target in marked_states:
        rev_target = target[::-1]
        zero_inds = [ind for ind in range(num_qubits) if rev_target.startswith("0", ind)]
        oracle.x(zero_inds)
        oracle.compose(MCMT(ZGate(), num_qubits - 1, 1), inplace=True)
        oracle.x(zero_inds)

    # Repeat grover operator for amplitude amplification.
    grover_op = GroverOperator(oracle).decompose()
    optimal_num_iterations = math.floor(math.pi / 4 * math.sqrt(2**grover_op.num_qubits / len(marked_states)))
    rep_grover = grover_op.repeat(optimal_num_iterations).decompose()

    # Create uniform superposition.
    result = QuantumCircuit(grover_op.num_qubits)
    result.h(range(grover_op.num_qubits))
    result.compose(rep_grover, inplace=True)
    result.measure_all()

    return result


marked_states = ["011", "100"]
circuit = grover_circuit(marked_states)

backend = Aer.get_backend('statevector_simulator')
circuit = transpile(circuit, backend) # TODO: Add this to implementation of detectors
result = backend.run(circuit).result()
outputstate = result.get_statevector(circuit)

print(outputstate)