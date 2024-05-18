OPENQASM 2.0;
include "qelib1.inc";
qreg q[5];
creg c[5];
h q[2];
h q[1];
h q[4];
u(0.02,pi,pi) q[1];
u(1.31,pi,pi) q[4];
cswap q[2],q[1],q[4];
h q[2];
measure q[2] -> c[2];
