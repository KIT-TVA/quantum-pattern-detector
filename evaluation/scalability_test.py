"""Methods for evaluating the scalability of the pattern detectors."""

import os, sys
parent_dir: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir + "/src")

from abstract_detector import PatternDetector
from state_prep import AngleEncodingDetector, BasisEncodingDetector
from quantum_states import EntanglementDetector, UniformSuperpositionDetector
from unitary_transformation import PhaseEstimationDetector, UncomputeDetector
from measurement import PostSelectiveMeasurementDetector
from io import TextIOWrapper

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

    elif sys.argv[1] == "BasisEncoding" or sys.argv[1] == "AngleEncoding":
        set_num = 2

    elif sys.argv[1] == "QuantumPhaseEstimation" or sys.argv[1] == "PostSelectiveMeasurement":
        set_num = 3

    elif sys.argv[1] == "Uncompute":
        set_num = 4

    else:
        raise ValueError("There is no support for detecting the given quantum pattern.")

    name_map: dict[str, PatternDetector] = {"UniformSuperposition": UniformSuperpositionDetector,
                                            "CreatingEntanglement": EntanglementDetector,
                                            "BasisEncoding": BasisEncodingDetector,
                                            "AngleEncoding": AngleEncodingDetector,
                                            "QuantumPhaseEstimation": PhaseEstimationDetector,
                                            "Uncompute": UncomputeDetector,
                                            "PostSelectiveMeasurement": PostSelectiveMeasurementDetector}

    for version in range(1, 14):
        input_file: TextIOWrapper = open(get_file_path("ghz", set_num, version))

        start_time: float = time.time()
        detector: PatternDetector = name_map[sys.argv[1]](input_file)
        detector.build_message()

        print("Version {v}: {time} seconds".format(v=version, time=time.time()-start_time))
