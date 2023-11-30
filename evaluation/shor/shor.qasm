OPENQASM 2.0;
include "qelib1.inc";
gate gate_QFT q0,q1,q2 { h q2; cp(pi/2) q2,q1; cp(pi/4) q2,q0; h q1; cp(pi/2) q1,q0; h q0; }
gate gate_QFT_1709803455568 q0,q1,q2 { gate_QFT q0,q1,q2; }
gate mcphase(param0) q0,q1,q2 { cp(0) q1,q2; cx q1,q0; cp(0) q0,q2; cx q1,q0; cp(0) q0,q2; }
gate mcphase_1709803523408(param0) q0,q1,q2 { cp(pi/2) q1,q2; cx q1,q0; cp(-pi/2) q0,q2; cx q1,q0; cp(pi/2) q0,q2; }
gate mcphase_1709803525584(param0) q0,q1,q2 { cp(pi/4) q1,q2; cx q1,q0; cp(-pi/4) q0,q2; cx q1,q0; cp(pi/4) q0,q2; }
gate ccphi_add_a(param0,param1,param2) q0,q1,q2,q3,q4 { mcphase(0) q0,q1,q2; mcphase_1709803523408(pi) q0,q1,q3; mcphase_1709803525584(pi/2) q0,q1,q4; }
gate phi_add_a_dg q0,q1,q2 { p(-3*pi/4) q2; p(-3*pi/2) q1; p(-pi) q0; }
gate gate_QFT_dg q0,q1,q2 { h q0; cp(-pi/2) q1,q0; h q1; cp(-pi/4) q2,q0; cp(-pi/2) q2,q1; h q2; }
gate gate_QFT_dg_1709803530768 q0,q1,q2 { gate_QFT_dg q0,q1,q2; }
gate gate_QFT_1709803565520 q0,q1,q2 { gate_QFT q0,q1,q2; }
gate mcphase_1709804192528(param0) q0,q1 { cp(pi) q0,q1; }
gate mcphase_1709804192784(param0) q0,q1 { cp(3*pi/2) q0,q1; }
gate mcphase_1709804192336(param0) q0,q1 { cp(3*pi/4) q0,q1; }
gate cphi_add_a q0,q1,q2,q3 { mcphase_1709804192528(pi) q0,q1; mcphase_1709804192784(3*pi/2) q0,q2; mcphase_1709804192336(3*pi/4) q0,q3; }
gate mcphase_1709804207184(param0) q0,q1,q2 { cp(-pi/2) q1,q2; cx q1,q0; cp(pi/2) q0,q2; cx q1,q0; cp(-pi/2) q0,q2; }
gate mcphase_1709804202704(param0) q0,q1,q2 { cp(-pi/4) q1,q2; cx q1,q0; cp(pi/4) q0,q2; cx q1,q0; cp(-pi/4) q0,q2; }
gate ccphi_add_a_dg(param0,param1,param2) q0,q1,q2,q3,q4 { mcphase(0) q0,q1,q2; mcphase_1709804207184(-pi) q0,q1,q3; mcphase_1709804202704(-pi/2) q0,q1,q4; }
gate gate_QFT_dg_1709803456528 q0,q1,q2 { gate_QFT_dg q0,q1,q2; }
gate gate_QFT_1709766985296 q0,q1,q2 { gate_QFT q0,q1,q2; }
gate ccphi_add_a_mod_N_188 q0,q1,q2,q3,q4,q5 { ccphi_add_a(0,pi,pi/2) q0,q1,q2,q3,q4; phi_add_a_dg q2,q3,q4; gate_QFT_dg_1709803530768 q2,q3,q4; cx q4,q5; gate_QFT_1709803565520 q2,q3,q4; cphi_add_a q5,q2,q3,q4; ccphi_add_a_dg(0,pi,pi/2) q0,q1,q2,q3,q4; gate_QFT_dg_1709803456528 q2,q3,q4; x q4; cx q4,q5; x q4; gate_QFT_1709766985296 q2,q3,q4; ccphi_add_a(0,pi,pi/2) q0,q1,q2,q3,q4; }
gate mcphase_1709804995600(param0) q0,q1,q2 { cp(pi/2) q1,q2; cx q1,q0; cp(-pi/2) q0,q2; cx q1,q0; cp(pi/2) q0,q2; }
gate mcphase_1709805003408(param0) q0,q1,q2 { cp(pi/4) q1,q2; cx q1,q0; cp(-pi/4) q0,q2; cx q1,q0; cp(pi/4) q0,q2; }
gate mcphase_1709804411408(param0) q0,q1,q2 { cp(pi/8) q1,q2; cx q1,q0; cp(-pi/8) q0,q2; cx q1,q0; cp(pi/8) q0,q2; }
gate ccphi_add_a_1709804194256(param0,param1,param2) q0,q1,q2,q3,q4 { mcphase_1709804995600(pi) q0,q1,q2; mcphase_1709805003408(pi/2) q0,q1,q3; mcphase_1709804411408(pi/4) q0,q1,q4; }
gate gate_QFT_dg_1709804242832 q0,q1,q2 { gate_QFT_dg q0,q1,q2; }
gate gate_QFT_1709804244240 q0,q1,q2 { gate_QFT q0,q1,q2; }
gate mcphase_1709804452880(param0) q0,q1,q2 { cp(-pi/2) q1,q2; cx q1,q0; cp(pi/2) q0,q2; cx q1,q0; cp(-pi/2) q0,q2; }
gate mcphase_1709804447760(param0) q0,q1,q2 { cp(-pi/4) q1,q2; cx q1,q0; cp(pi/4) q0,q2; cx q1,q0; cp(-pi/4) q0,q2; }
gate mcphase_1709804452240(param0) q0,q1,q2 { cp(-pi/8) q1,q2; cx q1,q0; cp(pi/8) q0,q2; cx q1,q0; cp(-pi/8) q0,q2; }
gate ccphi_add_a_dg_1709804446032(param0,param1,param2) q0,q1,q2,q3,q4 { mcphase_1709804452880(-pi) q0,q1,q2; mcphase_1709804447760(-pi/2) q0,q1,q3; mcphase_1709804452240(-pi/4) q0,q1,q4; }
gate gate_QFT_dg_1709804480336 q0,q1,q2 { gate_QFT_dg q0,q1,q2; }
gate gate_QFT_1709804479824 q0,q1,q2 { gate_QFT q0,q1,q2; }
gate mcphase_1709804492944(param0) q0,q1,q2 { cp(pi/2) q1,q2; cx q1,q0; cp(-pi/2) q0,q2; cx q1,q0; cp(pi/2) q0,q2; }
gate mcphase_1709804492880(param0) q0,q1,q2 { cp(pi/4) q1,q2; cx q1,q0; cp(-pi/4) q0,q2; cx q1,q0; cp(pi/4) q0,q2; }
gate mcphase_1709804490640(param0) q0,q1,q2 { cp(pi/8) q1,q2; cx q1,q0; cp(-pi/8) q0,q2; cx q1,q0; cp(pi/8) q0,q2; }
gate ccphi_add_a_1709804453776(param0,param1,param2) q0,q1,q2,q3,q4 { mcphase_1709804492944(pi) q0,q1,q2; mcphase_1709804492880(pi/2) q0,q1,q3; mcphase_1709804490640(pi/4) q0,q1,q4; }
gate ccphi_add_a_mod_N_191 q0,q1,q2,q3,q4,q5 { ccphi_add_a_1709804194256(pi,pi/2,pi/4) q0,q1,q2,q3,q4; phi_add_a_dg q2,q3,q4; gate_QFT_dg_1709804242832 q2,q3,q4; cx q4,q5; gate_QFT_1709804244240 q2,q3,q4; cphi_add_a q5,q2,q3,q4; ccphi_add_a_dg_1709804446032(pi,pi/2,pi/4) q0,q1,q2,q3,q4; gate_QFT_dg_1709804480336 q2,q3,q4; x q4; cx q4,q5; x q4; gate_QFT_1709804479824 q2,q3,q4; ccphi_add_a_1709804453776(pi,pi/2,pi/4) q0,q1,q2,q3,q4; }
gate gate_QFT_dg_1709804167504 q0,q1,q2 { gate_QFT_dg q0,q1,q2; }
gate gate_QFT_1709804530320 q0,q1,q2 { gate_QFT q0,q1,q2; }
gate mcphase_1709804565968(param0) q0,q1,q2 { cp(-pi/2) q1,q2; cx q1,q0; cp(pi/2) q0,q2; cx q1,q0; cp(-pi/2) q0,q2; }
gate mcphase_1709804559120(param0) q0,q1,q2 { cp(-pi/4) q1,q2; cx q1,q0; cp(pi/4) q0,q2; cx q1,q0; cp(-pi/4) q0,q2; }
gate mcphase_1709804564432(param0) q0,q1,q2 { cp(-pi/8) q1,q2; cx q1,q0; cp(pi/8) q0,q2; cx q1,q0; cp(-pi/8) q0,q2; }
gate ccphi_add_a_dg_1709804561232(param0,param1,param2) q0,q1,q2,q3,q4 { mcphase_1709804565968(-pi) q0,q1,q2; mcphase_1709804559120(-pi/2) q0,q1,q3; mcphase_1709804564432(-pi/4) q0,q1,q4; }
gate gate_QFT_dg_1709804542416 q0,q1,q2 { gate_QFT_dg q0,q1,q2; }
gate gate_QFT_1709804426000 q0,q1,q2 { gate_QFT q0,q1,q2; }
gate mcphase_1709804844688(param0) q0,q1,q2 { cp(pi/2) q1,q2; cx q1,q0; cp(-pi/2) q0,q2; cx q1,q0; cp(pi/2) q0,q2; }
gate mcphase_1709804836176(param0) q0,q1,q2 { cp(pi/4) q1,q2; cx q1,q0; cp(-pi/4) q0,q2; cx q1,q0; cp(pi/4) q0,q2; }
gate mcphase_1709804843728(param0) q0,q1,q2 { cp(pi/8) q1,q2; cx q1,q0; cp(-pi/8) q0,q2; cx q1,q0; cp(pi/8) q0,q2; }
gate ccphi_add_a_1709804786448(param0,param1,param2) q0,q1,q2,q3,q4 { mcphase_1709804844688(pi) q0,q1,q2; mcphase_1709804836176(pi/2) q0,q1,q3; mcphase_1709804843728(pi/4) q0,q1,q4; }
gate mcphase_1709804428816(param0) q0,q1 { cp(-pi) q0,q1; }
gate mcphase_1709804427152(param0) q0,q1 { cp(-3*pi/2) q0,q1; }
gate mcphase_1709804430480(param0) q0,q1 { cp(-3*pi/4) q0,q1; }
gate cphi_add_a_dg q0,q1,q2,q3 { mcphase_1709804428816(-pi) q0,q1; mcphase_1709804427152(-3*pi/2) q0,q2; mcphase_1709804430480(-3*pi/4) q0,q3; }
gate gate_QFT_dg_1709804856208 q0,q1,q2 { gate_QFT_dg q0,q1,q2; }
gate gate_QFT_1709804842256 q0,q1,q2 { gate_QFT q0,q1,q2; }
gate phi_add_a q0,q1,q2 { p(pi) q0; p(3*pi/2) q1; p(3*pi/4) q2; }
gate mcphase_1709804700624(param0) q0,q1,q2 { cp(-pi/2) q1,q2; cx q1,q0; cp(pi/2) q0,q2; cx q1,q0; cp(-pi/2) q0,q2; }
gate mcphase_1709804701008(param0) q0,q1,q2 { cp(-pi/4) q1,q2; cx q1,q0; cp(pi/4) q0,q2; cx q1,q0; cp(-pi/4) q0,q2; }
gate mcphase_1709804714320(param0) q0,q1,q2 { cp(-pi/8) q1,q2; cx q1,q0; cp(pi/8) q0,q2; cx q1,q0; cp(-pi/8) q0,q2; }
gate ccphi_add_a_dg_1709804851472(param0,param1,param2) q0,q1,q2,q3,q4 { mcphase_1709804700624(-pi) q0,q1,q2; mcphase_1709804701008(-pi/2) q0,q1,q3; mcphase_1709804714320(-pi/4) q0,q1,q4; }
gate ccphi_add_a_mod_N_dg_223 q0,q1,q2,q3,q4,q5 { ccphi_add_a_dg_1709804561232(pi,pi/2,pi/4) q0,q1,q2,q3,q4; gate_QFT_dg_1709804542416 q2,q3,q4; x q4; cx q4,q5; x q4; gate_QFT_1709804426000 q2,q3,q4; ccphi_add_a_1709804786448(pi,pi/2,pi/4) q0,q1,q2,q3,q4; cphi_add_a_dg q5,q2,q3,q4; gate_QFT_dg_1709804856208 q2,q3,q4; cx q4,q5; gate_QFT_1709804842256 q2,q3,q4; phi_add_a q2,q3,q4; ccphi_add_a_dg_1709804851472(pi,pi/2,pi/4) q0,q1,q2,q3,q4; }
gate gate_QFT_dg_1709803477392 q0,q1,q2 { gate_QFT_dg q0,q1,q2; }
gate gate_QFT_1709802521040 q0,q1,q2 { gate_QFT q0,q1,q2; }
gate gate_QFT_dg_1709802827984 q0,q1,q2 { gate_QFT_dg q0,q1,q2; }
gate gate_QFT_1709805103760 q0,q1,q2 { gate_QFT q0,q1,q2; }
gate ccphi_add_a_mod_N_dg_226 q0,q1,q2,q3,q4,q5 { ccphi_add_a_dg(0,pi,pi/2) q0,q1,q2,q3,q4; gate_QFT_dg_1709803477392 q2,q3,q4; x q4; cx q4,q5; x q4; gate_QFT_1709802521040 q2,q3,q4; ccphi_add_a(0,pi,pi/2) q0,q1,q2,q3,q4; cphi_add_a_dg q5,q2,q3,q4; gate_QFT_dg_1709802827984 q2,q3,q4; cx q4,q5; gate_QFT_1709805103760 q2,q3,q4; phi_add_a q2,q3,q4; ccphi_add_a_dg(0,pi,pi/2) q0,q1,q2,q3,q4; }
gate gate_QFT_dg_1709805540304 q0,q1,q2 { gate_QFT_dg q0,q1,q2; }
gate cmult_a_mod_N q0,q1,q2,q3,q4,q5,q6 { gate_QFT_1709803455568 q3,q4,q5; ccphi_add_a_mod_N_188 q0,q1,q3,q4,q5,q6; ccphi_add_a_mod_N_191 q0,q2,q3,q4,q5,q6; gate_QFT_dg_1709804167504 q3,q4,q5; cswap q0,q1,q3; cswap q0,q2,q4; gate_QFT_1709804530320 q3,q4,q5; ccphi_add_a_mod_N_dg_223 q0,q2,q3,q4,q5,q6; ccphi_add_a_mod_N_dg_226 q0,q1,q3,q4,q5,q6; gate_QFT_dg_1709805540304 q3,q4,q5; }
gate gate_QFT_1709802791888 q0,q1,q2 { gate_QFT q0,q1,q2; }
gate mcphase_1709807027664(param0) q0,q1,q2 { cp(pi/2) q1,q2; cx q1,q0; cp(-pi/2) q0,q2; cx q1,q0; cp(pi/2) q0,q2; }
gate mcphase_1709807333584(param0) q0,q1,q2 { cp(pi/4) q1,q2; cx q1,q0; cp(-pi/4) q0,q2; cx q1,q0; cp(pi/4) q0,q2; }
gate mcphase_1709807334800(param0) q0,q1,q2 { cp(pi/8) q1,q2; cx q1,q0; cp(-pi/8) q0,q2; cx q1,q0; cp(pi/8) q0,q2; }
gate ccphi_add_a_1709802370192(param0,param1,param2) q0,q1,q2,q3,q4 { mcphase_1709807027664(pi) q0,q1,q2; mcphase_1709807333584(pi/2) q0,q1,q3; mcphase_1709807334800(pi/4) q0,q1,q4; }
gate gate_QFT_dg_1709806168400 q0,q1,q2 { gate_QFT_dg q0,q1,q2; }
gate gate_QFT_1709802551248 q0,q1,q2 { gate_QFT q0,q1,q2; }
gate mcphase_1709806123984(param0) q0,q1,q2 { cp(-pi/2) q1,q2; cx q1,q0; cp(pi/2) q0,q2; cx q1,q0; cp(-pi/2) q0,q2; }
gate mcphase_1709805941904(param0) q0,q1,q2 { cp(-pi/4) q1,q2; cx q1,q0; cp(pi/4) q0,q2; cx q1,q0; cp(-pi/4) q0,q2; }
gate mcphase_1709805931664(param0) q0,q1,q2 { cp(-pi/8) q1,q2; cx q1,q0; cp(pi/8) q0,q2; cx q1,q0; cp(-pi/8) q0,q2; }
gate ccphi_add_a_dg_1709805923280(param0,param1,param2) q0,q1,q2,q3,q4 { mcphase_1709806123984(-pi) q0,q1,q2; mcphase_1709805941904(-pi/2) q0,q1,q3; mcphase_1709805931664(-pi/4) q0,q1,q4; }
gate gate_QFT_dg_1709766414288 q0,q1,q2 { gate_QFT_dg q0,q1,q2; }
gate gate_QFT_1709802670352 q0,q1,q2 { gate_QFT q0,q1,q2; }
gate mcphase_1709802753744(param0) q0,q1,q2 { cp(pi/2) q1,q2; cx q1,q0; cp(-pi/2) q0,q2; cx q1,q0; cp(pi/2) q0,q2; }
gate mcphase_1709802762640(param0) q0,q1,q2 { cp(pi/4) q1,q2; cx q1,q0; cp(-pi/4) q0,q2; cx q1,q0; cp(pi/4) q0,q2; }
gate mcphase_1709802742928(param0) q0,q1,q2 { cp(pi/8) q1,q2; cx q1,q0; cp(-pi/8) q0,q2; cx q1,q0; cp(pi/8) q0,q2; }
gate ccphi_add_a_1709802760464(param0,param1,param2) q0,q1,q2,q3,q4 { mcphase_1709802753744(pi) q0,q1,q2; mcphase_1709802762640(pi/2) q0,q1,q3; mcphase_1709802742928(pi/4) q0,q1,q4; }
gate ccphi_add_a_mod_N_250 q0,q1,q2,q3,q4,q5 { ccphi_add_a_1709802370192(pi,pi/2,pi/4) q0,q1,q2,q3,q4; phi_add_a_dg q2,q3,q4; gate_QFT_dg_1709806168400 q2,q3,q4; cx q4,q5; gate_QFT_1709802551248 q2,q3,q4; cphi_add_a q5,q2,q3,q4; ccphi_add_a_dg_1709805923280(pi,pi/2,pi/4) q0,q1,q2,q3,q4; gate_QFT_dg_1709766414288 q2,q3,q4; x q4; cx q4,q5; x q4; gate_QFT_1709802670352 q2,q3,q4; ccphi_add_a_1709802760464(pi,pi/2,pi/4) q0,q1,q2,q3,q4; }
gate mcphase_1709802103184(param0) q0,q1,q2 { cp(pi/2) q1,q2; cx q1,q0; cp(-pi/2) q0,q2; cx q1,q0; cp(pi/2) q0,q2; }
gate mcphase_1709802098960(param0) q0,q1,q2 { cp(pi/4) q1,q2; cx q1,q0; cp(-pi/4) q0,q2; cx q1,q0; cp(pi/4) q0,q2; }
gate ccphi_add_a_1709802762064(param0,param1,param2) q0,q1,q2,q3,q4 { mcphase(0) q0,q1,q2; mcphase_1709802103184(pi) q0,q1,q3; mcphase_1709802098960(pi/2) q0,q1,q4; }
gate gate_QFT_dg_1709802204048 q0,q1,q2 { gate_QFT_dg q0,q1,q2; }
gate gate_QFT_1709801980688 q0,q1,q2 { gate_QFT q0,q1,q2; }
gate mcphase_1709801990544(param0) q0,q1,q2 { cp(-pi/2) q1,q2; cx q1,q0; cp(pi/2) q0,q2; cx q1,q0; cp(-pi/2) q0,q2; }
gate mcphase_1709801991824(param0) q0,q1,q2 { cp(-pi/4) q1,q2; cx q1,q0; cp(pi/4) q0,q2; cx q1,q0; cp(-pi/4) q0,q2; }
gate ccphi_add_a_dg_1709801995792(param0,param1,param2) q0,q1,q2,q3,q4 { mcphase(0) q0,q1,q2; mcphase_1709801990544(-pi) q0,q1,q3; mcphase_1709801991824(-pi/2) q0,q1,q4; }
gate gate_QFT_dg_1709802107856 q0,q1,q2 { gate_QFT_dg q0,q1,q2; }
gate gate_QFT_1709802683152 q0,q1,q2 { gate_QFT q0,q1,q2; }
gate mcphase_1709802033296(param0) q0,q1,q2 { cp(pi/2) q1,q2; cx q1,q0; cp(-pi/2) q0,q2; cx q1,q0; cp(pi/2) q0,q2; }
gate mcphase_1709802034640(param0) q0,q1,q2 { cp(pi/4) q1,q2; cx q1,q0; cp(-pi/4) q0,q2; cx q1,q0; cp(pi/4) q0,q2; }
gate ccphi_add_a_1709801989008(param0,param1,param2) q0,q1,q2,q3,q4 { mcphase(0) q0,q1,q2; mcphase_1709802033296(pi) q0,q1,q3; mcphase_1709802034640(pi/2) q0,q1,q4; }
gate ccphi_add_a_mod_N_253 q0,q1,q2,q3,q4,q5 { ccphi_add_a_1709802762064(0,pi,pi/2) q0,q1,q2,q3,q4; phi_add_a_dg q2,q3,q4; gate_QFT_dg_1709802204048 q2,q3,q4; cx q4,q5; gate_QFT_1709801980688 q2,q3,q4; cphi_add_a q5,q2,q3,q4; ccphi_add_a_dg_1709801995792(0,pi,pi/2) q0,q1,q2,q3,q4; gate_QFT_dg_1709802107856 q2,q3,q4; x q4; cx q4,q5; x q4; gate_QFT_1709802683152 q2,q3,q4; ccphi_add_a_1709801989008(0,pi,pi/2) q0,q1,q2,q3,q4; }
gate gate_QFT_dg_1709801985296 q0,q1,q2 { gate_QFT_dg q0,q1,q2; }
gate gate_QFT_1709801879824 q0,q1,q2 { gate_QFT q0,q1,q2; }
gate mcphase_1709801818896(param0) q0,q1,q2 { cp(-pi/2) q1,q2; cx q1,q0; cp(pi/2) q0,q2; cx q1,q0; cp(-pi/2) q0,q2; }
gate mcphase_1709801830096(param0) q0,q1,q2 { cp(-pi/4) q1,q2; cx q1,q0; cp(pi/4) q0,q2; cx q1,q0; cp(-pi/4) q0,q2; }
gate ccphi_add_a_dg_1709801851984(param0,param1,param2) q0,q1,q2,q3,q4 { mcphase(0) q0,q1,q2; mcphase_1709801818896(-pi) q0,q1,q3; mcphase_1709801830096(-pi/2) q0,q1,q4; }
gate gate_QFT_dg_1709801470928 q0,q1,q2 { gate_QFT_dg q0,q1,q2; }
gate gate_QFT_1709801599952 q0,q1,q2 { gate_QFT q0,q1,q2; }
gate mcphase_1709801077328(param0) q0,q1,q2 { cp(pi/2) q1,q2; cx q1,q0; cp(-pi/2) q0,q2; cx q1,q0; cp(pi/2) q0,q2; }
gate mcphase_1709801062864(param0) q0,q1,q2 { cp(pi/4) q1,q2; cx q1,q0; cp(-pi/4) q0,q2; cx q1,q0; cp(pi/4) q0,q2; }
gate ccphi_add_a_1709801386128(param0,param1,param2) q0,q1,q2,q3,q4 { mcphase(0) q0,q1,q2; mcphase_1709801077328(pi) q0,q1,q3; mcphase_1709801062864(pi/2) q0,q1,q4; }
gate gate_QFT_dg_1709801738448 q0,q1,q2 { gate_QFT_dg q0,q1,q2; }
gate gate_QFT_1709801818640 q0,q1,q2 { gate_QFT q0,q1,q2; }
gate mcphase_1709801628240(param0) q0,q1,q2 { cp(-pi/2) q1,q2; cx q1,q0; cp(pi/2) q0,q2; cx q1,q0; cp(-pi/2) q0,q2; }
gate mcphase_1709801633040(param0) q0,q1,q2 { cp(-pi/4) q1,q2; cx q1,q0; cp(pi/4) q0,q2; cx q1,q0; cp(-pi/4) q0,q2; }
gate ccphi_add_a_dg_1709801624656(param0,param1,param2) q0,q1,q2,q3,q4 { mcphase(0) q0,q1,q2; mcphase_1709801628240(-pi) q0,q1,q3; mcphase_1709801633040(-pi/2) q0,q1,q4; }
gate ccphi_add_a_mod_N_dg_285 q0,q1,q2,q3,q4,q5 { ccphi_add_a_dg_1709801851984(0,pi,pi/2) q0,q1,q2,q3,q4; gate_QFT_dg_1709801470928 q2,q3,q4; x q4; cx q4,q5; x q4; gate_QFT_1709801599952 q2,q3,q4; ccphi_add_a_1709801386128(0,pi,pi/2) q0,q1,q2,q3,q4; cphi_add_a_dg q5,q2,q3,q4; gate_QFT_dg_1709801738448 q2,q3,q4; cx q4,q5; gate_QFT_1709801818640 q2,q3,q4; phi_add_a q2,q3,q4; ccphi_add_a_dg_1709801624656(0,pi,pi/2) q0,q1,q2,q3,q4; }
gate mcphase_1709801652624(param0) q0,q1,q2 { cp(-pi/2) q1,q2; cx q1,q0; cp(pi/2) q0,q2; cx q1,q0; cp(-pi/2) q0,q2; }
gate mcphase_1709801225872(param0) q0,q1,q2 { cp(-pi/4) q1,q2; cx q1,q0; cp(pi/4) q0,q2; cx q1,q0; cp(-pi/4) q0,q2; }
gate mcphase_1709801165840(param0) q0,q1,q2 { cp(-pi/8) q1,q2; cx q1,q0; cp(pi/8) q0,q2; cx q1,q0; cp(-pi/8) q0,q2; }
gate ccphi_add_a_dg_1709801627984(param0,param1,param2) q0,q1,q2,q3,q4 { mcphase_1709801652624(-pi) q0,q1,q2; mcphase_1709801225872(-pi/2) q0,q1,q3; mcphase_1709801165840(-pi/4) q0,q1,q4; }
gate gate_QFT_dg_1709807910800 q0,q1,q2 { gate_QFT_dg q0,q1,q2; }
gate gate_QFT_1709807950288 q0,q1,q2 { gate_QFT q0,q1,q2; }
gate mcphase_1709807865616(param0) q0,q1,q2 { cp(pi/2) q1,q2; cx q1,q0; cp(-pi/2) q0,q2; cx q1,q0; cp(pi/2) q0,q2; }
gate mcphase_1709807865808(param0) q0,q1,q2 { cp(pi/4) q1,q2; cx q1,q0; cp(-pi/4) q0,q2; cx q1,q0; cp(pi/4) q0,q2; }
gate mcphase_1709807866512(param0) q0,q1,q2 { cp(pi/8) q1,q2; cx q1,q0; cp(-pi/8) q0,q2; cx q1,q0; cp(pi/8) q0,q2; }
gate ccphi_add_a_1709807908368(param0,param1,param2) q0,q1,q2,q3,q4 { mcphase_1709807865616(pi) q0,q1,q2; mcphase_1709807865808(pi/2) q0,q1,q3; mcphase_1709807866512(pi/4) q0,q1,q4; }
gate gate_QFT_dg_1709807863504 q0,q1,q2 { gate_QFT_dg q0,q1,q2; }
gate gate_QFT_1709800944400 q0,q1,q2 { gate_QFT q0,q1,q2; }
gate mcphase_1709807956112(param0) q0,q1,q2 { cp(-pi/2) q1,q2; cx q1,q0; cp(pi/2) q0,q2; cx q1,q0; cp(-pi/2) q0,q2; }
gate mcphase_1709807956304(param0) q0,q1,q2 { cp(-pi/4) q1,q2; cx q1,q0; cp(pi/4) q0,q2; cx q1,q0; cp(-pi/4) q0,q2; }
gate mcphase_1709807957008(param0) q0,q1,q2 { cp(-pi/8) q1,q2; cx q1,q0; cp(pi/8) q0,q2; cx q1,q0; cp(-pi/8) q0,q2; }
gate ccphi_add_a_dg_1709807949776(param0,param1,param2) q0,q1,q2,q3,q4 { mcphase_1709807956112(-pi) q0,q1,q2; mcphase_1709807956304(-pi/2) q0,q1,q3; mcphase_1709807957008(-pi/4) q0,q1,q4; }
gate ccphi_add_a_mod_N_dg_288 q0,q1,q2,q3,q4,q5 { ccphi_add_a_dg_1709801627984(pi,pi/2,pi/4) q0,q1,q2,q3,q4; gate_QFT_dg_1709807910800 q2,q3,q4; x q4; cx q4,q5; x q4; gate_QFT_1709807950288 q2,q3,q4; ccphi_add_a_1709807908368(pi,pi/2,pi/4) q0,q1,q2,q3,q4; cphi_add_a_dg q5,q2,q3,q4; gate_QFT_dg_1709807863504 q2,q3,q4; cx q4,q5; gate_QFT_1709800944400 q2,q3,q4; phi_add_a q2,q3,q4; ccphi_add_a_dg_1709807949776(pi,pi/2,pi/4) q0,q1,q2,q3,q4; }
gate gate_QFT_dg_1709804821648 q0,q1,q2 { gate_QFT_dg q0,q1,q2; }
gate cmult_a_mod_N_1709806550608 q0,q1,q2,q3,q4,q5,q6 { gate_QFT_1709802791888 q3,q4,q5; ccphi_add_a_mod_N_250 q0,q1,q3,q4,q5,q6; ccphi_add_a_mod_N_253 q0,q2,q3,q4,q5,q6; gate_QFT_dg_1709801985296 q3,q4,q5; cswap q0,q1,q3; cswap q0,q2,q4; gate_QFT_1709801879824 q3,q4,q5; ccphi_add_a_mod_N_dg_285 q0,q2,q3,q4,q5,q6; ccphi_add_a_mod_N_dg_288 q0,q1,q3,q4,q5,q6; gate_QFT_dg_1709804821648 q3,q4,q5; }
gate gate_QFT_1709808275600 q0,q1,q2 { gate_QFT q0,q1,q2; }
gate mcphase_1709807325712(param0) q0,q1,q2 { cp(pi/2) q1,q2; cx q1,q0; cp(-pi/2) q0,q2; cx q1,q0; cp(pi/2) q0,q2; }
gate mcphase_1709806014160(param0) q0,q1,q2 { cp(pi/4) q1,q2; cx q1,q0; cp(-pi/4) q0,q2; cx q1,q0; cp(pi/4) q0,q2; }
gate mcphase_1709806025552(param0) q0,q1,q2 { cp(pi/8) q1,q2; cx q1,q0; cp(-pi/8) q0,q2; cx q1,q0; cp(pi/8) q0,q2; }
gate ccphi_add_a_1709800945488(param0,param1,param2) q0,q1,q2,q3,q4 { mcphase_1709807325712(pi) q0,q1,q2; mcphase_1709806014160(pi/2) q0,q1,q3; mcphase_1709806025552(pi/4) q0,q1,q4; }
gate gate_QFT_dg_1709807076816 q0,q1,q2 { gate_QFT_dg q0,q1,q2; }
gate gate_QFT_1709806115728 q0,q1,q2 { gate_QFT q0,q1,q2; }
gate mcphase_1709802549392(param0) q0,q1,q2 { cp(-pi/2) q1,q2; cx q1,q0; cp(pi/2) q0,q2; cx q1,q0; cp(-pi/2) q0,q2; }
gate mcphase_1709802362256(param0) q0,q1,q2 { cp(-pi/4) q1,q2; cx q1,q0; cp(pi/4) q0,q2; cx q1,q0; cp(-pi/4) q0,q2; }
gate mcphase_1709802358480(param0) q0,q1,q2 { cp(-pi/8) q1,q2; cx q1,q0; cp(pi/8) q0,q2; cx q1,q0; cp(-pi/8) q0,q2; }
gate ccphi_add_a_dg_1709805939344(param0,param1,param2) q0,q1,q2,q3,q4 { mcphase_1709802549392(-pi) q0,q1,q2; mcphase_1709802362256(-pi/2) q0,q1,q3; mcphase_1709802358480(-pi/4) q0,q1,q4; }
gate gate_QFT_dg_1709808103696 q0,q1,q2 { gate_QFT_dg q0,q1,q2; }
gate gate_QFT_1709805856912 q0,q1,q2 { gate_QFT q0,q1,q2; }
gate mcphase_1709808322832(param0) q0,q1,q2 { cp(pi/2) q1,q2; cx q1,q0; cp(-pi/2) q0,q2; cx q1,q0; cp(pi/2) q0,q2; }
gate mcphase_1709808323088(param0) q0,q1,q2 { cp(pi/4) q1,q2; cx q1,q0; cp(-pi/4) q0,q2; cx q1,q0; cp(pi/4) q0,q2; }
gate mcphase_1709808323600(param0) q0,q1,q2 { cp(pi/8) q1,q2; cx q1,q0; cp(-pi/8) q0,q2; cx q1,q0; cp(pi/8) q0,q2; }
gate ccphi_add_a_1709805748624(param0,param1,param2) q0,q1,q2,q3,q4 { mcphase_1709808322832(pi) q0,q1,q2; mcphase_1709808323088(pi/2) q0,q1,q3; mcphase_1709808323600(pi/4) q0,q1,q4; }
gate ccphi_add_a_mod_N_312 q0,q1,q2,q3,q4,q5 { ccphi_add_a_1709800945488(pi,pi/2,pi/4) q0,q1,q2,q3,q4; phi_add_a_dg q2,q3,q4; gate_QFT_dg_1709807076816 q2,q3,q4; cx q4,q5; gate_QFT_1709806115728 q2,q3,q4; cphi_add_a q5,q2,q3,q4; ccphi_add_a_dg_1709805939344(pi,pi/2,pi/4) q0,q1,q2,q3,q4; gate_QFT_dg_1709808103696 q2,q3,q4; x q4; cx q4,q5; x q4; gate_QFT_1709805856912 q2,q3,q4; ccphi_add_a_1709805748624(pi,pi/2,pi/4) q0,q1,q2,q3,q4; }
gate mcphase_1709808464080(param0) q0,q1,q2 { cp(pi/2) q1,q2; cx q1,q0; cp(-pi/2) q0,q2; cx q1,q0; cp(pi/2) q0,q2; }
gate mcphase_1709808456016(param0) q0,q1,q2 { cp(pi/4) q1,q2; cx q1,q0; cp(-pi/4) q0,q2; cx q1,q0; cp(pi/4) q0,q2; }
gate ccphi_add_a_1709805758096(param0,param1,param2) q0,q1,q2,q3,q4 { mcphase(0) q0,q1,q2; mcphase_1709808464080(pi) q0,q1,q3; mcphase_1709808456016(pi/2) q0,q1,q4; }
gate gate_QFT_dg_1709808600784 q0,q1,q2 { gate_QFT_dg q0,q1,q2; }
gate gate_QFT_1709808553680 q0,q1,q2 { gate_QFT q0,q1,q2; }
gate mcphase_1709808555344(param0) q0,q1,q2 { cp(-pi/2) q1,q2; cx q1,q0; cp(pi/2) q0,q2; cx q1,q0; cp(-pi/2) q0,q2; }
gate mcphase_1709808556048(param0) q0,q1,q2 { cp(-pi/4) q1,q2; cx q1,q0; cp(pi/4) q0,q2; cx q1,q0; cp(-pi/4) q0,q2; }
gate ccphi_add_a_dg_1709808464528(param0,param1,param2) q0,q1,q2,q3,q4 { mcphase(0) q0,q1,q2; mcphase_1709808555344(-pi) q0,q1,q3; mcphase_1709808556048(-pi/2) q0,q1,q4; }
gate gate_QFT_dg_1709808559568 q0,q1,q2 { gate_QFT_dg q0,q1,q2; }
gate gate_QFT_1709808663696 q0,q1,q2 { gate_QFT q0,q1,q2; }
gate mcphase_1709808563984(param0) q0,q1,q2 { cp(pi/2) q1,q2; cx q1,q0; cp(-pi/2) q0,q2; cx q1,q0; cp(pi/2) q0,q2; }
gate mcphase_1709808564688(param0) q0,q1,q2 { cp(pi/4) q1,q2; cx q1,q0; cp(-pi/4) q0,q2; cx q1,q0; cp(pi/4) q0,q2; }
gate ccphi_add_a_1709808559056(param0,param1,param2) q0,q1,q2,q3,q4 { mcphase(0) q0,q1,q2; mcphase_1709808563984(pi) q0,q1,q3; mcphase_1709808564688(pi/2) q0,q1,q4; }
gate ccphi_add_a_mod_N_315 q0,q1,q2,q3,q4,q5 { ccphi_add_a_1709805758096(0,pi,pi/2) q0,q1,q2,q3,q4; phi_add_a_dg q2,q3,q4; gate_QFT_dg_1709808600784 q2,q3,q4; cx q4,q5; gate_QFT_1709808553680 q2,q3,q4; cphi_add_a q5,q2,q3,q4; ccphi_add_a_dg_1709808464528(0,pi,pi/2) q0,q1,q2,q3,q4; gate_QFT_dg_1709808559568 q2,q3,q4; x q4; cx q4,q5; x q4; gate_QFT_1709808663696 q2,q3,q4; ccphi_add_a_1709808559056(0,pi,pi/2) q0,q1,q2,q3,q4; }
gate gate_QFT_dg_1709808560976 q0,q1,q2 { gate_QFT_dg q0,q1,q2; }
gate gate_QFT_1709808826256 q0,q1,q2 { gate_QFT q0,q1,q2; }
gate mcphase_1709808833680(param0) q0,q1,q2 { cp(-pi/2) q1,q2; cx q1,q0; cp(pi/2) q0,q2; cx q1,q0; cp(-pi/2) q0,q2; }
gate mcphase_1709808843088(param0) q0,q1,q2 { cp(-pi/4) q1,q2; cx q1,q0; cp(pi/4) q0,q2; cx q1,q0; cp(-pi/4) q0,q2; }
gate ccphi_add_a_dg_1709808842640(param0,param1,param2) q0,q1,q2,q3,q4 { mcphase(0) q0,q1,q2; mcphase_1709808833680(-pi) q0,q1,q3; mcphase_1709808843088(-pi/2) q0,q1,q4; }
gate gate_QFT_dg_1709808965008 q0,q1,q2 { gate_QFT_dg q0,q1,q2; }
gate gate_QFT_1709808475152 q0,q1,q2 { gate_QFT q0,q1,q2; }
gate mcphase_1709808929104(param0) q0,q1,q2 { cp(pi/2) q1,q2; cx q1,q0; cp(-pi/2) q0,q2; cx q1,q0; cp(pi/2) q0,q2; }
gate mcphase_1709808930192(param0) q0,q1,q2 { cp(pi/4) q1,q2; cx q1,q0; cp(-pi/4) q0,q2; cx q1,q0; cp(pi/4) q0,q2; }
gate ccphi_add_a_1709808888336(param0,param1,param2) q0,q1,q2,q3,q4 { mcphase(0) q0,q1,q2; mcphase_1709808929104(pi) q0,q1,q3; mcphase_1709808930192(pi/2) q0,q1,q4; }
gate gate_QFT_dg_1709808845968 q0,q1,q2 { gate_QFT_dg q0,q1,q2; }
gate gate_QFT_1709808999184 q0,q1,q2 { gate_QFT q0,q1,q2; }
gate mcphase_1709808984016(param0) q0,q1,q2 { cp(-pi/2) q1,q2; cx q1,q0; cp(pi/2) q0,q2; cx q1,q0; cp(-pi/2) q0,q2; }
gate mcphase_1709808984720(param0) q0,q1,q2 { cp(-pi/4) q1,q2; cx q1,q0; cp(pi/4) q0,q2; cx q1,q0; cp(-pi/4) q0,q2; }
gate ccphi_add_a_dg_1709808977616(param0,param1,param2) q0,q1,q2,q3,q4 { mcphase(0) q0,q1,q2; mcphase_1709808984016(-pi) q0,q1,q3; mcphase_1709808984720(-pi/2) q0,q1,q4; }
gate ccphi_add_a_mod_N_dg_347 q0,q1,q2,q3,q4,q5 { ccphi_add_a_dg_1709808842640(0,pi,pi/2) q0,q1,q2,q3,q4; gate_QFT_dg_1709808965008 q2,q3,q4; x q4; cx q4,q5; x q4; gate_QFT_1709808475152 q2,q3,q4; ccphi_add_a_1709808888336(0,pi,pi/2) q0,q1,q2,q3,q4; cphi_add_a_dg q5,q2,q3,q4; gate_QFT_dg_1709808845968 q2,q3,q4; cx q4,q5; gate_QFT_1709808999184 q2,q3,q4; phi_add_a q2,q3,q4; ccphi_add_a_dg_1709808977616(0,pi,pi/2) q0,q1,q2,q3,q4; }
gate mcphase_1709809100688(param0) q0,q1,q2 { cp(-pi/2) q1,q2; cx q1,q0; cp(pi/2) q0,q2; cx q1,q0; cp(-pi/2) q0,q2; }
gate mcphase_1709809149200(param0) q0,q1,q2 { cp(-pi/4) q1,q2; cx q1,q0; cp(pi/4) q0,q2; cx q1,q0; cp(-pi/4) q0,q2; }
gate mcphase_1709809149968(param0) q0,q1,q2 { cp(-pi/8) q1,q2; cx q1,q0; cp(pi/8) q0,q2; cx q1,q0; cp(-pi/8) q0,q2; }
gate ccphi_add_a_dg_1709808662160(param0,param1,param2) q0,q1,q2,q3,q4 { mcphase_1709809100688(-pi) q0,q1,q2; mcphase_1709809149200(-pi/2) q0,q1,q3; mcphase_1709809149968(-pi/4) q0,q1,q4; }
gate gate_QFT_dg_1709809260816 q0,q1,q2 { gate_QFT_dg q0,q1,q2; }
gate gate_QFT_1709809371152 q0,q1,q2 { gate_QFT q0,q1,q2; }
gate mcphase_1709809316880(param0) q0,q1,q2 { cp(pi/2) q1,q2; cx q1,q0; cp(-pi/2) q0,q2; cx q1,q0; cp(pi/2) q0,q2; }
gate mcphase_1709809317072(param0) q0,q1,q2 { cp(pi/4) q1,q2; cx q1,q0; cp(-pi/4) q0,q2; cx q1,q0; cp(pi/4) q0,q2; }
gate mcphase_1709809317776(param0) q0,q1,q2 { cp(pi/8) q1,q2; cx q1,q0; cp(-pi/8) q0,q2; cx q1,q0; cp(pi/8) q0,q2; }
gate ccphi_add_a_1709809310672(param0,param1,param2) q0,q1,q2,q3,q4 { mcphase_1709809316880(pi) q0,q1,q2; mcphase_1709809317072(pi/2) q0,q1,q3; mcphase_1709809317776(pi/4) q0,q1,q4; }
gate gate_QFT_dg_1709809374032 q0,q1,q2 { gate_QFT_dg q0,q1,q2; }
gate gate_QFT_1709808660752 q0,q1,q2 { gate_QFT q0,q1,q2; }
gate mcphase_1709809373264(param0) q0,q1,q2 { cp(-pi/2) q1,q2; cx q1,q0; cp(pi/2) q0,q2; cx q1,q0; cp(-pi/2) q0,q2; }
gate mcphase_1709809373456(param0) q0,q1,q2 { cp(-pi/4) q1,q2; cx q1,q0; cp(pi/4) q0,q2; cx q1,q0; cp(-pi/4) q0,q2; }
gate mcphase_1709809374160(param0) q0,q1,q2 { cp(-pi/8) q1,q2; cx q1,q0; cp(pi/8) q0,q2; cx q1,q0; cp(-pi/8) q0,q2; }
gate ccphi_add_a_dg_1709809366992(param0,param1,param2) q0,q1,q2,q3,q4 { mcphase_1709809373264(-pi) q0,q1,q2; mcphase_1709809373456(-pi/2) q0,q1,q3; mcphase_1709809374160(-pi/4) q0,q1,q4; }
gate ccphi_add_a_mod_N_dg_350 q0,q1,q2,q3,q4,q5 { ccphi_add_a_dg_1709808662160(pi,pi/2,pi/4) q0,q1,q2,q3,q4; gate_QFT_dg_1709809260816 q2,q3,q4; x q4; cx q4,q5; x q4; gate_QFT_1709809371152 q2,q3,q4; ccphi_add_a_1709809310672(pi,pi/2,pi/4) q0,q1,q2,q3,q4; cphi_add_a_dg q5,q2,q3,q4; gate_QFT_dg_1709809374032 q2,q3,q4; cx q4,q5; gate_QFT_1709808660752 q2,q3,q4; phi_add_a q2,q3,q4; ccphi_add_a_dg_1709809366992(pi,pi/2,pi/4) q0,q1,q2,q3,q4; }
gate gate_QFT_dg_1709801353168 q0,q1,q2 { gate_QFT_dg q0,q1,q2; }
gate cmult_a_mod_N_1709806877456 q0,q1,q2,q3,q4,q5,q6 { gate_QFT_1709808275600 q3,q4,q5; ccphi_add_a_mod_N_312 q0,q1,q3,q4,q5,q6; ccphi_add_a_mod_N_315 q0,q2,q3,q4,q5,q6; gate_QFT_dg_1709808560976 q3,q4,q5; cswap q0,q1,q3; cswap q0,q2,q4; gate_QFT_1709808826256 q3,q4,q5; ccphi_add_a_mod_N_dg_347 q0,q2,q3,q4,q5,q6; ccphi_add_a_mod_N_dg_350 q0,q1,q3,q4,q5,q6; gate_QFT_dg_1709801353168 q3,q4,q5; }
gate gate_QFT_1709809685072 q0,q1,q2 { gate_QFT q0,q1,q2; }
gate mcphase_1709805850896(param0) q0,q1,q2 { cp(pi/2) q1,q2; cx q1,q0; cp(-pi/2) q0,q2; cx q1,q0; cp(pi/2) q0,q2; }
gate mcphase_1709805590544(param0) q0,q1,q2 { cp(pi/4) q1,q2; cx q1,q0; cp(-pi/4) q0,q2; cx q1,q0; cp(pi/4) q0,q2; }
gate mcphase_1709805759760(param0) q0,q1,q2 { cp(pi/8) q1,q2; cx q1,q0; cp(-pi/8) q0,q2; cx q1,q0; cp(pi/8) q0,q2; }
gate ccphi_add_a_1709805941392(param0,param1,param2) q0,q1,q2,q3,q4 { mcphase_1709805850896(pi) q0,q1,q2; mcphase_1709805590544(pi/2) q0,q1,q3; mcphase_1709805759760(pi/4) q0,q1,q4; }
gate gate_QFT_dg_1709809592272 q0,q1,q2 { gate_QFT_dg q0,q1,q2; }
gate gate_QFT_1709809493648 q0,q1,q2 { gate_QFT q0,q1,q2; }
gate mcphase_1709805456528(param0) q0,q1,q2 { cp(-pi/2) q1,q2; cx q1,q0; cp(pi/2) q0,q2; cx q1,q0; cp(-pi/2) q0,q2; }
gate mcphase_1709809555664(param0) q0,q1,q2 { cp(-pi/4) q1,q2; cx q1,q0; cp(pi/4) q0,q2; cx q1,q0; cp(-pi/4) q0,q2; }
gate mcphase_1709809555088(param0) q0,q1,q2 { cp(-pi/8) q1,q2; cx q1,q0; cp(pi/8) q0,q2; cx q1,q0; cp(-pi/8) q0,q2; }
gate ccphi_add_a_dg_1709805065680(param0,param1,param2) q0,q1,q2,q3,q4 { mcphase_1709805456528(-pi) q0,q1,q2; mcphase_1709809555664(-pi/2) q0,q1,q3; mcphase_1709809555088(-pi/4) q0,q1,q4; }
gate gate_QFT_dg_1709801063952 q0,q1,q2 { gate_QFT_dg q0,q1,q2; }
gate gate_QFT_1709807146512 q0,q1,q2 { gate_QFT q0,q1,q2; }
gate mcphase_1709809538512(param0) q0,q1,q2 { cp(pi/2) q1,q2; cx q1,q0; cp(-pi/2) q0,q2; cx q1,q0; cp(pi/2) q0,q2; }
gate mcphase_1709806932560(param0) q0,q1,q2 { cp(pi/4) q1,q2; cx q1,q0; cp(-pi/4) q0,q2; cx q1,q0; cp(pi/4) q0,q2; }
gate mcphase_1709807867472(param0) q0,q1,q2 { cp(pi/8) q1,q2; cx q1,q0; cp(-pi/8) q0,q2; cx q1,q0; cp(pi/8) q0,q2; }
gate ccphi_add_a_1709808273872(param0,param1,param2) q0,q1,q2,q3,q4 { mcphase_1709809538512(pi) q0,q1,q2; mcphase_1709806932560(pi/2) q0,q1,q3; mcphase_1709807867472(pi/4) q0,q1,q4; }
gate ccphi_add_a_mod_N_374 q0,q1,q2,q3,q4,q5 { ccphi_add_a_1709805941392(pi,pi/2,pi/4) q0,q1,q2,q3,q4; phi_add_a_dg q2,q3,q4; gate_QFT_dg_1709809592272 q2,q3,q4; cx q4,q5; gate_QFT_1709809493648 q2,q3,q4; cphi_add_a q5,q2,q3,q4; ccphi_add_a_dg_1709805065680(pi,pi/2,pi/4) q0,q1,q2,q3,q4; gate_QFT_dg_1709801063952 q2,q3,q4; x q4; cx q4,q5; x q4; gate_QFT_1709807146512 q2,q3,q4; ccphi_add_a_1709808273872(pi,pi/2,pi/4) q0,q1,q2,q3,q4; }
gate mcphase_1709804957392(param0) q0,q1,q2 { cp(pi/2) q1,q2; cx q1,q0; cp(-pi/2) q0,q2; cx q1,q0; cp(pi/2) q0,q2; }
gate mcphase_1709804945936(param0) q0,q1,q2 { cp(pi/4) q1,q2; cx q1,q0; cp(-pi/4) q0,q2; cx q1,q0; cp(pi/4) q0,q2; }
gate ccphi_add_a_1709807867088(param0,param1,param2) q0,q1,q2,q3,q4 { mcphase(0) q0,q1,q2; mcphase_1709804957392(pi) q0,q1,q3; mcphase_1709804945936(pi/2) q0,q1,q4; }
gate gate_QFT_dg_1709801913744 q0,q1,q2 { gate_QFT_dg q0,q1,q2; }
gate gate_QFT_1709801347728 q0,q1,q2 { gate_QFT q0,q1,q2; }
gate mcphase_1709801789392(param0) q0,q1,q2 { cp(-pi/2) q1,q2; cx q1,q0; cp(pi/2) q0,q2; cx q1,q0; cp(-pi/2) q0,q2; }
gate mcphase_1709803256592(param0) q0,q1,q2 { cp(-pi/4) q1,q2; cx q1,q0; cp(pi/4) q0,q2; cx q1,q0; cp(-pi/4) q0,q2; }
gate ccphi_add_a_dg_1709801913616(param0,param1,param2) q0,q1,q2,q3,q4 { mcphase(0) q0,q1,q2; mcphase_1709801789392(-pi) q0,q1,q3; mcphase_1709803256592(-pi/2) q0,q1,q4; }
gate gate_QFT_dg_1709804905232 q0,q1,q2 { gate_QFT_dg q0,q1,q2; }
gate gate_QFT_1709804772304 q0,q1,q2 { gate_QFT q0,q1,q2; }
gate mcphase_1709804634064(param0) q0,q1,q2 { cp(pi/2) q1,q2; cx q1,q0; cp(-pi/2) q0,q2; cx q1,q0; cp(pi/2) q0,q2; }
gate mcphase_1709804451536(param0) q0,q1,q2 { cp(pi/4) q1,q2; cx q1,q0; cp(-pi/4) q0,q2; cx q1,q0; cp(pi/4) q0,q2; }
gate ccphi_add_a_1709803383824(param0,param1,param2) q0,q1,q2,q3,q4 { mcphase(0) q0,q1,q2; mcphase_1709804634064(pi) q0,q1,q3; mcphase_1709804451536(pi/2) q0,q1,q4; }
gate ccphi_add_a_mod_N_377 q0,q1,q2,q3,q4,q5 { ccphi_add_a_1709807867088(0,pi,pi/2) q0,q1,q2,q3,q4; phi_add_a_dg q2,q3,q4; gate_QFT_dg_1709801913744 q2,q3,q4; cx q4,q5; gate_QFT_1709801347728 q2,q3,q4; cphi_add_a q5,q2,q3,q4; ccphi_add_a_dg_1709801913616(0,pi,pi/2) q0,q1,q2,q3,q4; gate_QFT_dg_1709804905232 q2,q3,q4; x q4; cx q4,q5; x q4; gate_QFT_1709804772304 q2,q3,q4; ccphi_add_a_1709803383824(0,pi,pi/2) q0,q1,q2,q3,q4; }
gate gate_QFT_dg_1709804439056 q0,q1,q2 { gate_QFT_dg q0,q1,q2; }
gate gate_QFT_1709804154576 q0,q1,q2 { gate_QFT q0,q1,q2; }
gate mcphase_1709805757072(param0) q0,q1,q2 { cp(-pi/2) q1,q2; cx q1,q0; cp(pi/2) q0,q2; cx q1,q0; cp(-pi/2) q0,q2; }
gate mcphase_1709805750736(param0) q0,q1,q2 { cp(-pi/4) q1,q2; cx q1,q0; cp(pi/4) q0,q2; cx q1,q0; cp(-pi/4) q0,q2; }
gate ccphi_add_a_dg_1709801744208(param0,param1,param2) q0,q1,q2,q3,q4 { mcphase(0) q0,q1,q2; mcphase_1709805757072(-pi) q0,q1,q3; mcphase_1709805750736(-pi/2) q0,q1,q4; }
gate gate_QFT_dg_1709809539728 q0,q1,q2 { gate_QFT_dg q0,q1,q2; }
gate gate_QFT_1709809711888 q0,q1,q2 { gate_QFT q0,q1,q2; }
gate mcphase_1709805593872(param0) q0,q1,q2 { cp(pi/2) q1,q2; cx q1,q0; cp(-pi/2) q0,q2; cx q1,q0; cp(pi/2) q0,q2; }
gate mcphase_1709805585488(param0) q0,q1,q2 { cp(pi/4) q1,q2; cx q1,q0; cp(-pi/4) q0,q2; cx q1,q0; cp(pi/4) q0,q2; }
gate ccphi_add_a_1709806107920(param0,param1,param2) q0,q1,q2,q3,q4 { mcphase(0) q0,q1,q2; mcphase_1709805593872(pi) q0,q1,q3; mcphase_1709805585488(pi/2) q0,q1,q4; }
gate gate_QFT_dg_1709809852304 q0,q1,q2 { gate_QFT_dg q0,q1,q2; }
gate gate_QFT_1709803567376 q0,q1,q2 { gate_QFT q0,q1,q2; }
gate mcphase_1709809850064(param0) q0,q1,q2 { cp(-pi/2) q1,q2; cx q1,q0; cp(pi/2) q0,q2; cx q1,q0; cp(-pi/2) q0,q2; }
gate mcphase_1709809850768(param0) q0,q1,q2 { cp(-pi/4) q1,q2; cx q1,q0; cp(pi/4) q0,q2; cx q1,q0; cp(-pi/4) q0,q2; }
gate ccphi_add_a_dg_1709809843472(param0,param1,param2) q0,q1,q2,q3,q4 { mcphase(0) q0,q1,q2; mcphase_1709809850064(-pi) q0,q1,q3; mcphase_1709809850768(-pi/2) q0,q1,q4; }
gate ccphi_add_a_mod_N_dg_409 q0,q1,q2,q3,q4,q5 { ccphi_add_a_dg_1709801744208(0,pi,pi/2) q0,q1,q2,q3,q4; gate_QFT_dg_1709809539728 q2,q3,q4; x q4; cx q4,q5; x q4; gate_QFT_1709809711888 q2,q3,q4; ccphi_add_a_1709806107920(0,pi,pi/2) q0,q1,q2,q3,q4; cphi_add_a_dg q5,q2,q3,q4; gate_QFT_dg_1709809852304 q2,q3,q4; cx q4,q5; gate_QFT_1709803567376 q2,q3,q4; phi_add_a q2,q3,q4; ccphi_add_a_dg_1709809843472(0,pi,pi/2) q0,q1,q2,q3,q4; }
gate mcphase_1709802157392(param0) q0,q1,q2 { cp(-pi/2) q1,q2; cx q1,q0; cp(pi/2) q0,q2; cx q1,q0; cp(-pi/2) q0,q2; }
gate mcphase_1709806102928(param0) q0,q1,q2 { cp(-pi/4) q1,q2; cx q1,q0; cp(pi/4) q0,q2; cx q1,q0; cp(-pi/4) q0,q2; }
gate mcphase_1709805675280(param0) q0,q1,q2 { cp(-pi/8) q1,q2; cx q1,q0; cp(pi/8) q0,q2; cx q1,q0; cp(-pi/8) q0,q2; }
gate ccphi_add_a_dg_1709809839504(param0,param1,param2) q0,q1,q2,q3,q4 { mcphase_1709802157392(-pi) q0,q1,q2; mcphase_1709806102928(-pi/2) q0,q1,q3; mcphase_1709805675280(-pi/4) q0,q1,q4; }
gate gate_QFT_dg_1709810153616 q0,q1,q2 { gate_QFT_dg q0,q1,q2; }
gate gate_QFT_1709810193680 q0,q1,q2 { gate_QFT q0,q1,q2; }
gate mcphase_1709810158160(param0) q0,q1,q2 { cp(pi/2) q1,q2; cx q1,q0; cp(-pi/2) q0,q2; cx q1,q0; cp(pi/2) q0,q2; }
gate mcphase_1709810158352(param0) q0,q1,q2 { cp(pi/4) q1,q2; cx q1,q0; cp(-pi/4) q0,q2; cx q1,q0; cp(pi/4) q0,q2; }
gate mcphase_1709810159056(param0) q0,q1,q2 { cp(pi/8) q1,q2; cx q1,q0; cp(-pi/8) q0,q2; cx q1,q0; cp(pi/8) q0,q2; }
gate ccphi_add_a_1709810151760(param0,param1,param2) q0,q1,q2,q3,q4 { mcphase_1709810158160(pi) q0,q1,q2; mcphase_1709810158352(pi/2) q0,q1,q3; mcphase_1709810159056(pi/4) q0,q1,q4; }
gate gate_QFT_dg_1709810113552 q0,q1,q2 { gate_QFT_dg q0,q1,q2; }
gate gate_QFT_1709802364432 q0,q1,q2 { gate_QFT q0,q1,q2; }
gate mcphase_1709810199504(param0) q0,q1,q2 { cp(-pi/2) q1,q2; cx q1,q0; cp(pi/2) q0,q2; cx q1,q0; cp(-pi/2) q0,q2; }
gate mcphase_1709810199696(param0) q0,q1,q2 { cp(-pi/4) q1,q2; cx q1,q0; cp(pi/4) q0,q2; cx q1,q0; cp(-pi/4) q0,q2; }
gate mcphase_1709810200400(param0) q0,q1,q2 { cp(-pi/8) q1,q2; cx q1,q0; cp(pi/8) q0,q2; cx q1,q0; cp(-pi/8) q0,q2; }
gate ccphi_add_a_dg_1709810193168(param0,param1,param2) q0,q1,q2,q3,q4 { mcphase_1709810199504(-pi) q0,q1,q2; mcphase_1709810199696(-pi/2) q0,q1,q3; mcphase_1709810200400(-pi/4) q0,q1,q4; }
gate ccphi_add_a_mod_N_dg_412 q0,q1,q2,q3,q4,q5 { ccphi_add_a_dg_1709809839504(pi,pi/2,pi/4) q0,q1,q2,q3,q4; gate_QFT_dg_1709810153616 q2,q3,q4; x q4; cx q4,q5; x q4; gate_QFT_1709810193680 q2,q3,q4; ccphi_add_a_1709810151760(pi,pi/2,pi/4) q0,q1,q2,q3,q4; cphi_add_a_dg q5,q2,q3,q4; gate_QFT_dg_1709810113552 q2,q3,q4; cx q4,q5; gate_QFT_1709802364432 q2,q3,q4; phi_add_a q2,q3,q4; ccphi_add_a_dg_1709810193168(pi,pi/2,pi/4) q0,q1,q2,q3,q4; }
gate gate_QFT_dg_1709809957648 q0,q1,q2 { gate_QFT_dg q0,q1,q2; }
gate cmult_a_mod_N_1709807172560 q0,q1,q2,q3,q4,q5,q6 { gate_QFT_1709809685072 q3,q4,q5; ccphi_add_a_mod_N_374 q0,q1,q3,q4,q5,q6; ccphi_add_a_mod_N_377 q0,q2,q3,q4,q5,q6; gate_QFT_dg_1709804439056 q3,q4,q5; cswap q0,q1,q3; cswap q0,q2,q4; gate_QFT_1709804154576 q3,q4,q5; ccphi_add_a_mod_N_dg_409 q0,q2,q3,q4,q5,q6; ccphi_add_a_mod_N_dg_412 q0,q1,q3,q4,q5,q6; gate_QFT_dg_1709809957648 q3,q4,q5; }
gate gate_IQFT q0,q1,q2,q3 { swap q1,q2; swap q0,q3; h q0; cp(-pi/2) q1,q0; h q1; cp(-pi/4) q2,q0; cp(-pi/2) q2,q1; h q2; cp(-pi/8) q3,q0; cp(-pi/4) q3,q1; cp(-pi/2) q3,q2; h q3; }
gate gate_IQFT_1709806660560 q0,q1,q2,q3 { gate_IQFT q0,q1,q2,q3; }
qreg up[4];
qreg down[2];
qreg aux[4];
creg meas[10];
h up[0];
h up[1];
h up[2];
h up[3];
x down[0];
cmult_a_mod_N up[0],down[0],down[1],aux[0],aux[1],aux[2],aux[3];
cmult_a_mod_N_1709806550608 up[1],down[0],down[1],aux[0],aux[1],aux[2],aux[3];
cmult_a_mod_N_1709806877456 up[2],down[0],down[1],aux[0],aux[1],aux[2],aux[3];
cmult_a_mod_N_1709807172560 up[3],down[0],down[1],aux[0],aux[1],aux[2],aux[3];
gate_IQFT_1709806660560 up[0],up[1],up[2],up[3];
barrier up[0],up[1],up[2],up[3],down[0],down[1],aux[0],aux[1],aux[2],aux[3];
measure up[0] -> meas[0];
measure up[1] -> meas[1];
measure up[2] -> meas[2];
measure up[3] -> meas[3];
measure down[0] -> meas[4];
measure down[1] -> meas[5];
measure aux[0] -> meas[6];
measure aux[1] -> meas[7];
measure aux[2] -> meas[8];
measure aux[3] -> meas[9];
