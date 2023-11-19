from state_prep import AngleEncodingDetector, BasisEncodingDetector
from quantum_states import EntanglementDetector, UniformSuperpositionDetector
from unitary_transformation import PhaseEstimationDetector, UncomputeDetector
from measurement import PostSelectiveMeasurementDetector

from io import TextIOWrapper

if __name__ == '__main__':
    input_file: TextIOWrapper = open("C:/quantum-pattern-detector/code-example.txt")
    msg: str = PostSelectiveMeasurementDetector(input_file).build_message()
    print(msg)