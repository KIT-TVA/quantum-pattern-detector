OPENQASM 2.0;
include "qelib1.inc";
qreg q0[2];
ry(pi/4) q0[0];
cx q0[1],q0[0];
ry(pi/4) q0[0];
cx q0[1],q0[0];