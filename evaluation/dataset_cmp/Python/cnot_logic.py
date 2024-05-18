"""Uses CNOT to implement some logic."""
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit.circuit.library.standard_gates import XGate
from qiskit_aer import AerSimulator


register1 = QuantumRegister(3)
register2 = QuantumRegister(3)
register3 = QuantumRegister(3)

circuit = QuantumCircuit(register1, register2, register3)

# c = not c
circuit.x(register1[2])

# if (b) then c = not c
circuit.x(register2[1])
circuit.cx(register2[1], register2[2])

# if (a and b) then c = not c
circuit.x(register3[0])
circuit.x(register3[1])
circuit.ccx(register3[0], register3[1], register3[2])

circuit.measure_all()

simulator = AerSimulator()

compiled_circuit = transpile(circuit, simulator)

job = simulator.run(compiled_circuit, shots=1000)

result = job.result()
counts = result.get_counts(compiled_circuit)

print(counts)
