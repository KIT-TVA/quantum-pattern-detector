OPENQASM 2.0;
include "qelib1.inc";
gate gate_QFT q0,q1,q2,q3 { h q3; cp(pi/2) q3,q2; cp(pi/4) q3,q1; cp(pi/8) q3,q0; h q2; cp(pi/2) q2,q1; cp(pi/4) q2,q0; h q1; cp(pi/2) q1,q0; h q0; }
gate gate_QFT_2140119875856 q0,q1,q2,q3 { gate_QFT q0,q1,q2,q3; }
gate mcphase(param0) q0,q1,q2 { cp(2*pi) q1,q2; cx q1,q0; cp(-2*pi) q0,q2; cx q1,q0; cp(2*pi) q0,q2; }
gate mcphase_2140119949328(param0) q0,q1,q2 { cp(pi) q1,q2; cx q1,q0; cp(-pi) q0,q2; cx q1,q0; cp(pi) q0,q2; }
gate mcphase_2140119946512(param0) q0,q1,q2 { cp(pi/2) q1,q2; cx q1,q0; cp(-pi/2) q0,q2; cx q1,q0; cp(pi/2) q0,q2; }
gate mcphase_2140119949904(param0) q0,q1,q2 { cp(pi/4) q1,q2; cx q1,q0; cp(-pi/4) q0,q2; cx q1,q0; cp(pi/4) q0,q2; }
gate mcphase_2140119951376(param0) q0,q1,q2 { cp(pi) q1,q2; cx q1,q0; cp(-pi) q0,q2; cx q1,q0; cp(pi) q0,q2; }
gate mcphase_2140119951760(param0) q0,q1,q2 { cp(pi) q1,q2; cx q1,q0; cp(-pi) q0,q2; cx q1,q0; cp(pi) q0,q2; }
gate mcphase_2140119953296(param0) q0,q1,q2 { cp(pi/2) q1,q2; cx q1,q0; cp(-pi/2) q0,q2; cx q1,q0; cp(pi/2) q0,q2; }
gate mcphase_2140119941392(param0) q0,q1,q2 { cp(pi/2) q1,q2; cx q1,q0; cp(-pi/2) q0,q2; cx q1,q0; cp(pi/2) q0,q2; }
gate mcphase_2140119942608(param0) q0,q1,q2 { cp(pi/4) q1,q2; cx q1,q0; cp(-pi/4) q0,q2; cx q1,q0; cp(pi/4) q0,q2; }
gate mcphase_2140119945680(param0) q0,q1,q2 { cp(pi/4) q1,q2; cx q1,q0; cp(-pi/4) q0,q2; cx q1,q0; cp(pi/4) q0,q2; }
gate mcphase_2140119984848(param0) q0,q1,q2 { cp(pi/8) q1,q2; cx q1,q0; cp(-pi/8) q0,q2; cx q1,q0; cp(pi/8) q0,q2; }
gate mcphase_2140119985296(param0) q0,q1,q2 { cp(pi/8) q1,q2; cx q1,q0; cp(-pi/8) q0,q2; cx q1,q0; cp(pi/8) q0,q2; }
gate mcphase_2140119989840(param0) q0,q1,q2 { cp(pi/2) q1,q2; cx q1,q0; cp(-pi/2) q0,q2; cx q1,q0; cp(pi/2) q0,q2; }
gate mcphase_2140119976208(param0) q0,q1,q2 { cp(pi/4) q1,q2; cx q1,q0; cp(-pi/4) q0,q2; cx q1,q0; cp(pi/4) q0,q2; }
gate mcphase_2140119979344(param0) q0,q1,q2 { cp(pi/8) q1,q2; cx q1,q0; cp(-pi/8) q0,q2; cx q1,q0; cp(pi/8) q0,q2; }
gate mcphase_2140119987792(param0) q0,q1,q2 { cp(pi/16) q1,q2; cx q1,q0; cp(-pi/16) q0,q2; cx q1,q0; cp(pi/16) q0,q2; }
gate gate_IQFT q0,q1,q2,q3 { h q0; cp(-pi/2) q1,q0; h q1; cp(-pi/4) q2,q0; cp(-pi/2) q2,q1; h q2; cp(-pi/8) q3,q0; cp(-pi/4) q3,q1; cp(-pi/2) q3,q2; h q3; }       
gate gate_IQFT_2140119325904 q0,q1,q2,q3 { gate_IQFT q0,q1,q2,q3; }
qreg q[8];
creg c[4];
x q[1];
x q[2];
x q[3];
gate_QFT_2140119875856 q[4],q[5],q[6],q[7];
mcphase(4*pi) q[1],q[3],q[4];
mcphase_2140119949328(2*pi) q[1],q[3],q[5];
mcphase_2140119946512(pi) q[1],q[3],q[6];
mcphase_2140119949904(pi/2) q[1],q[3],q[7];
mcphase_2140119951376(2*pi) q[1],q[2],q[4];
mcphase_2140119951760(2*pi) q[0],q[3],q[4];
mcphase_2140119953296(pi) q[1],q[2],q[5];
mcphase_2140119941392(pi) q[0],q[3],q[5];
mcphase_2140119942608(pi/2) q[1],q[2],q[6];
mcphase_2140119945680(pi/2) q[0],q[3],q[6];
mcphase_2140119984848(pi/4) q[1],q[2],q[7];
mcphase_2140119985296(pi/4) q[0],q[3],q[7];
mcphase_2140119989840(pi) q[0],q[2],q[4];
mcphase_2140119976208(pi/2) q[0],q[2],q[5];
mcphase_2140119979344(pi/4) q[0],q[2],q[6];
mcphase_2140119987792(pi/8) q[0],q[2],q[7];
gate_IQFT_2140119325904 q[4],q[5],q[6],q[7];
measure q[4] -> c[0];
measure q[5] -> c[1];
measure q[6] -> c[2];
measure q[7] -> c[3];