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


def get_file_path(file_str: str, version: int) -> str:
    """Compute the path to the file with a certain name in the evaluation framework.
    
    Args:
        file_str (str): Name of the file.

    Returns:
        str: Path to the file with the name ```file_str``.
    """
    path_str: str = parent_dir + "/evaluation/"
    file_path: str = path_str + "feasibility" + "/" + file_str + str(version) + ".qasm"
    
    return file_path


for version in range(1, 14):
    input_file: TextIOWrapper = open(get_file_path("ghz", version))

    start_time: float = time.time()
    detector: PatternDetector = UncomputeDetector(input_file)
    detector.build_message()

    print("Version {v}: {time} seconds".format(v=version, time=time.time()-start_time))
