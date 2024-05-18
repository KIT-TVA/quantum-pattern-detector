OPENQASM 2.0;
include "qelib1.inc";
qreg q0[2];
h q0[0];
cx q0[0],q0[1];