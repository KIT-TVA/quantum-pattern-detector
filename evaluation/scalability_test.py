"""Methods for evaluating the scalability of the pattern detectors."""

import os, sys
parent_dir: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir + "/src")

from abstract_detector import PatternDetector
from state_prep import AngleEncodingDetector, BasisEncodingDetector, AmplitudeEncodingDetector
from quantum_states import EntanglementDetector, UniformSuperpositionDetector
from unitary_transformation import PhaseEstimationDetector, UncomputeDetector
from measurement import PostSelectiveMeasurementDetector

from qiskit import QuantumCircuit
from qiskit.circuit.random import random_circuit
import qiskit.qasm2 

import time

def get_file_path(file_str: str, set_num: int, version: int) -> str:
    """Compute the path to the file with a certain name in the evaluation framework.
    
    Args:
        file_str (str): Name of the file.
        set_num (int): Number of the evaluation set.
        version (int): Version number of the quantum circuit with the evaluation set.

    Returns:
        str: Path to the file with the name ```file_str``.
    """
    path_str: str = parent_dir + "/evaluation/"
    file_path: str = path_str + "feasibility" + str(set_num) + "/" + file_str + str(version) + ".qasm"
    
    return file_path


if __name__ == '__main__':

    set_num: int = 0

    if sys.argv[1] == "UniformSuperposition" or sys.argv[1] == "CreatingEntanglement":
        set_num = 1

    elif sys.argv[1] == "BasisEncoding" or sys.argv[1] == "AngleEncoding" or sys.argv[1] == "AmplitudeEncoding":
        set_num = 2

    elif sys.argv[1] == "QuantumPhaseEstimation" or sys.argv[1] == "PostSelectiveMeasurement":
        set_num = 3

    elif sys.argv[1] == "Uncompute":
        set_num = 4

    else:
        raise ValueError("There is no support for detecting the given quantum pattern.")

    name_map = {"UniformSuperposition": (UniformSuperpositionDetector, [1,2,3,4,5,6,7,8,9,10,11,12,13]),
                "CreatingEntanglement": (EntanglementDetector, [1,2,3,4,5,6,7,8,9,10,11,12,13]),
                "BasisEncoding": (BasisEncodingDetector, [1,5,10,25,50,100,125,150,200,300,500,1000]),
                "AngleEncoding": (AngleEncodingDetector, [1,5,10,25,50,100,125,150,200,300,500,1000]),
                "AmplitudeEncoding": (AmplitudeEncodingDetector, [1,5,10,25,50,100,125,150,200,300,500,1000]),
                "QuantumPhaseEstimation": (PhaseEstimationDetector, [1,5,10,25,50,100,125,150,200,300,500,1000]),
                "Uncompute": (UncomputeDetector, [1,3,5,10,15,20,25,30,40,50,60,70,100]),
                "PostSelectiveMeasurement": (PostSelectiveMeasurementDetector, [1,5,10,25,50,100,125,150,200,300,500,1000])}

#   for version in range(1, 14):
#        input_file: TextIOWrapper = open(get_file_path("ghz", set_num, version))

#        start_time: float = time.time()
#        detector: PatternDetector = name_map[sys.argv[1]](input_file)
#        detector.build_message()

#        print("Version {v}: {time} seconds".format(v=version, time=time.time()-start_time))

    print("Run 1: Constant depth, Increasing width.")
    for i in name_map[sys.argv[1]][1]:
        total_time: int = 0
        for j in range(0,20):
            circ: QuantumCircuit = random_circuit(i, 5)
            qiskit.qasm2.dump(circ, "scal_test.txt")
            detector: PatternDetector = name_map[sys.argv[1]][0](open("scal_test.txt"))
            start_time: float = time.time()
            detector.detect_pattern()
            total_time += time.time()-start_time
            
        print("Qubits {n}: {time} seconds".format(n=i, time=total_time / 20))

    print("Run 2: Constant width, Increasing depth.")
    for i in name_map[sys.argv[1]][1]:
        total_time: int = 0
        for j in range(0,20):
            circ: QuantumCircuit = random_circuit(3, i)
            qiskit.qasm2.dump(circ, "scal_test.txt")
            detector: PatternDetector = name_map[sys.argv[1]][0](open("scal_test.txt"))
            start_time: float = time.time()
            detector.detect_pattern()
            total_time += time.time()-start_time
            
        print("Qubits {n}: {time} seconds".format(n=i, time=total_time / 20))
        

