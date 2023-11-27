import os, sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir + "/src")

from state_prep import AngleEncodingDetector, BasisEncodingDetector
from quantum_states import EntanglementDetector, UniformSuperpositionDetector
from unitary_transformation import PhaseEstimationDetector, UncomputeDetector
from measurement import PostSelectiveMeasurementDetector

from io import TextIOWrapper


FILE_PATH: list = ["amplitude_estimation", "deutsch_jozsa", "ghz", "grover"]

def test_all() -> str:
    path_str: str = parent_dir + "/evaluation/"
    msg: str = ""

    for file_str in FILE_PATH:
        file_path = path_str + file_str + "/" + file_str + ".qasm"
        input_file: TextIOWrapper = open(file_path)
        msg += file_str + ":" + "\n" + \
                "---------------------------------" + "\n" + \
                UniformSuperpositionDetector(input_file).build_message() + "\n" + \
                EntanglementDetector(input_file).build_message() + "\n" + \
                BasisEncodingDetector(input_file).build_message() + "\n" + \
                AngleEncodingDetector(input_file).build_message() + "\n" + \
                PhaseEstimationDetector(input_file).build_message() + "\n" + \
                UncomputeDetector(input_file).build_message() + "\n" + \
                PostSelectiveMeasurementDetector(input_file).build_message() + "\n\n"
        
    return msg.strip()


if __name__ == '__main__':
    print(test_all())

        