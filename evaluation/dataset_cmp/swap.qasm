OPENQASM 2.0;
include "qelib1.inc";
qreg q[2];
rz(-1.570796) q[0];
sx q[0];
rz(-pi) q[0];
sx q[1];
rz(-0.82708959) q[1];
sx q[1];
rz(1.570796) q[1];
cx q[0],q[1];
sx q[0];
rz(0.595136487115318) q[1];
sx q[1];
rz(4.23624343718915) q[1];
sx q[1];
rz(10.0199144478847) q[1];
cx q[0],q[1];
rz(-pi) q[0];
sx q[0];
rz(1.570796) q[0];
rz(-2.46682769761062) q[1];
sx q[1];
rz(5.23398300598363) q[1];
sx q[1];
rz(12.0093564133491) q[1];
cx q[0],q[1];
rz(-3.14159) q[0];
sx q[0];
rz(-1.570796) q[0];
rz(1.570796) q[1];
sx q[1];
rz(-0.74370674) q[1];
