OPENQASM 2.0;
include "qelib1.inc";
qreg q[2];
sx q[0];
rz(-0.785398) q[0];
sx q[0];
rz(2.3145031) q[1];
sx q[1];
rz(1.570796) q[1];
cx q[0],q[1];
sx q[0];
rz(-0.785398) q[0];
sx q[0];
rz(1.570796) q[1];
sx q[1];
rz(-2.3145031) q[1];
