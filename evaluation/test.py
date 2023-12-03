import os, sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir + "/src")

from abstract_detector import PatternDetector
from state_prep import AngleEncodingDetector, BasisEncodingDetector
from quantum_states import EntanglementDetector, UniformSuperpositionDetector
from unitary_transformation import PhaseEstimationDetector, UncomputeDetector
from measurement import PostSelectiveMeasurementDetector

from io import TextIOWrapper


FILE_PATH: list = ["adder_with_overflow",
                   "adder_without_overflow",
                   "amplitude_estimation", 
                   "deutsch_jozsa", 
                   "ghz", 
                   "graph_state", 
                   "grover",
                   "hhl",
                   "multiplier",
                   "qaoa",
                   "qft",
                   "qft_entangled",
                   "quantum_phase_estimation",
                   "quantum_walk",
                   "real_amplitudes",
                   "shor",
                   "su2",
                   "variational_quantum_eigensolver",
                   "wstate"]

def all_messages() -> str:
    msg: str = ""

    for file_str in FILE_PATH:
        input_file: TextIOWrapper = open(get_file_path(file_str))
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

def all_metrics() -> str:
    return (metrics_ufs() + \
            metrics_entanglement() + \
            metrics_basis_encoding() + \
            metrics_angle_encoding() + \
            metrics_qpe() + \
            metrics_uncompute() + \
            metrics_psm()).strip()

def metrics_ufs() -> str:
    ground_truth: dict[str, list[(int, int)]] = \
        {"adder_with_overflow": [],
         "adder_without_overflow": [],
         "amplitude_estimation": [(6,9)], 
         "deutsch_jozsa": [(5,16)], 
         "ghz": [(5,5)], 
         "graph_state": [(5,13)], 
         "grover": [(7,16), (20,21), (24,26)],
         "hhl": [(11,18)],
         "multiplier": [],
         "qaoa": [(5,13)],
         "qft": [(5,17)],
         "qft_entangled": [(5,5), (14,17)],
         "quantum_phase_estimation": [(6,15)],
         "quantum_walk": [(6,7), (15,16), (21,23), (31,33)],
         "real_amplitudes": [],
         "shor": [(278,281)],
         "su2": [],
         "variational_quantum_eigensolver": [],
         "wstate": []}
    
    metrics: (int, int, int) = metrics_for_line_detectors(ground_truth, UniformSuperpositionDetector)

    return "Uniform superposition detector\n" + \
           "----------------------------------\n" +\
           "Precison: {p}, Recall: {r}, F-Measure: {f}\n".format(p=metrics[0], r=metrics[1], f=metrics[2])

def metrics_entanglement() -> str:
    ground_truth: dict[str, list[(int, int)]] = \
        {"adder_with_overflow": [],
         "adder_without_overflow": [],
         "amplitude_estimation": [(12,25)], 
         "deutsch_jozsa": [], 
         "ghz": [(6,9)], 
         "graph_state": [(7,15)], 
         "grover": [(11,33)],
         "hhl": [(26,501)],
         "multiplier": [],
         "qaoa": [(9,33)],
         "qft": [],
         "qft_entangled": [(6,23)],
         "quantum_phase_estimation": [(15,21)],
         "quantum_walk": [(8,29)],
         "real_amplitudes": [(7,27)],
         "shor": [(283,292)],
         "su2": [(9,30)],
         "variational_quantum_eigensolver": [(8,19)],
         "wstate": [(10,15)]}
    
    metrics: (float, float, float) = metrics_for_line_detectors(ground_truth, EntanglementDetector)

    return "Entanglement detector\n" + \
           "----------------------------------\n" +\
           "Precison: {p}, Recall: {r}, F-Measure: {f}\n".format(p=metrics[0], r=metrics[1], f=metrics[2])

def metrics_basis_encoding() -> str: 
    ground_truth: dict[str, bool] = \
        {"adder_with_overflow": True,
         "adder_without_overflow": True,
         "amplitude_estimation": False, 
         "deutsch_jozsa": False, 
         "ghz": False, 
         "graph_state": False, 
         "grover": False,
         "hhl": False,
         "multiplier": True,
         "qaoa": False,
         "qft": False,
         "qft_entangled": False,
         "quantum_phase_estimation": False,
         "quantum_walk": False,
         "real_amplitudes": False,
         "shor": False,
         "su2": False,
         "variational_quantum_eigensolver": False,
         "wstate": False}
    
    metrics: (float, float, float) = metrics_for_instance_detectors(ground_truth, BasisEncodingDetector, use_list=True)

    return "Basis encoding detector\n" + \
           "----------------------------------\n" +\
           "Precison: {p}, Recall: {r}, F-Measure: {f}\n".format(p=metrics[0], r=metrics[1], f=metrics[2])

def metrics_angle_encoding() -> str: 
    ground_truth: dict[str, bool] = \
        {"adder_with_overflow": False,
         "adder_without_overflow": False,
         "amplitude_estimation": False, 
         "deutsch_jozsa": False, 
         "ghz": False, 
         "graph_state": False, 
         "grover": False,
         "hhl": False,
         "multiplier": False,
         "qaoa": False,
         "qft": False,
         "qft_entangled": False,
         "quantum_phase_estimation": False,
         "quantum_walk": False,
         "real_amplitudes": True,
         "shor": False,
         "su2": True,
         "variational_quantum_eigensolver": True,
         "wstate": False}
    
    metrics: (float, float, float) = metrics_for_instance_detectors(ground_truth, AngleEncodingDetector, use_list=True)

    return "Angle encoding detector\n" + \
           "----------------------------------\n" +\
           "Precison: {p}, Recall: {r}, F-Measure: {f}\n".format(p=metrics[0], r=metrics[1], f=metrics[2])

def metrics_qpe() -> str: 
    ground_truth: dict[str, bool] = \
        {"adder_with_overflow": False,
         "adder_without_overflow": False,
         "amplitude_estimation": True, 
         "deutsch_jozsa": False, 
         "ghz": False, 
         "graph_state": False, 
         "grover": False,
         "hhl": True,
         "multiplier": False,
         "qaoa": False,
         "qft": False,
         "qft_entangled": False,
         "quantum_phase_estimation": True,
         "quantum_walk": False,
         "real_amplitudes": False,
         "shor": True,
         "su2": False,
         "variational_quantum_eigensolver": False,
         "wstate": False}
    
    metrics: (float, float, float) = metrics_for_instance_detectors(ground_truth, PhaseEstimationDetector)

    return "Quantum Phase Estimation detector\n" + \
           "----------------------------------\n" +\
           "Precison: {p}, Recall: {r}, F-Measure: {f}\n".format(p=metrics[0], r=metrics[1], f=metrics[2])

def metrics_uncompute() -> str: 
    ground_truth: dict[str, bool] = \
        {"adder_with_overflow": False,
         "adder_without_overflow": False,
         "amplitude_estimation": False, 
         "deutsch_jozsa": True, 
         "ghz": False, 
         "graph_state": False, 
         "grover": True,
         "hhl": True,
         "multiplier": False,
         "qaoa": False,
         "qft": False,
         "qft_entangled": False,
         "quantum_phase_estimation": False,
         "quantum_walk": True,
         "real_amplitudes": False,
         "shor": False,
         "su2": False,
         "variational_quantum_eigensolver": False,
         "wstate": False}
    
    metrics: (float, float, float) = metrics_for_instance_detectors(ground_truth, UncomputeDetector)

    return "Uncompute detector\n" + \
           "----------------------------------\n" +\
           "Precison: {p}, Recall: {r}, F-Measure: {f}\n".format(p=metrics[0], r=metrics[1], f=metrics[2])

def metrics_psm() -> str: 
    ground_truth: dict[str, bool] = \
        {"adder_with_overflow": False,
         "adder_without_overflow": False,
         "amplitude_estimation": False, 
         "deutsch_jozsa": False, 
         "ghz": False, 
         "graph_state": False, 
         "grover": False,
         "hhl": True,
         "multiplier": False,
         "qaoa": False,
         "qft": False,
         "qft_entangled": False,
         "quantum_phase_estimation": False,
         "quantum_walk": False,
         "real_amplitudes": False,
         "shor": False,
         "su2": False,
         "variational_quantum_eigensolver": False,
         "wstate": False}
    
    metrics: (float, float, float) = metrics_for_instance_detectors(
                                        ground_truth, 
                                        PostSelectiveMeasurementDetector, 
                                        use_list=True
                                    )

    return "Post Selctive Measurement detector\n" + \
           "----------------------------------\n" +\
           "Precison: {p}, Recall: {r}, F-Measure: {f}\n".format(p=metrics[0], r=metrics[1], f=metrics[2])

def get_file_path(file_str: str) -> str:
    path_str: str = parent_dir + "/evaluation/"
    file_path: str = path_str + file_str + "/" + file_str + ".qasm"
    
    return file_path

def calculate_metrics(tp: int, fp: int, fn: int) -> (float, float, float):

    precision: float = tp / (tp + fp)
    recall: float = tp / (tp + fn)
    f_measure: float = (2 * precision * recall) / (precision + recall)

    return (round(precision, 4), round(recall, 4), round(f_measure, 4))

def metrics_for_line_detectors(
        ground_truth: dict[str, list[(int, int)]], 
        detector: PatternDetector
    ) -> (float, float, float):
    
    true_positives: int = 0
    false_positives: int = 0
    false_negatives: int = 0

    for key, value in ground_truth.items():
        input_file: TextIOWrapper = open(get_file_path(key))
        detected_instances: list[(int, int)] = detector(input_file).detect_pattern()

        if value == detected_instances:
            true_positives += len(value)
            continue

        for instance in value:
            if instance in detected_instances:
                true_positives += 1
            else:
                false_negatives += 1

        for instance in detected_instances:
            if instance not in value:
                false_positives += 1

    return calculate_metrics(true_positives, false_positives, false_negatives)

def metrics_for_instance_detectors(
        ground_truth: dict[str, bool], 
        detector: PatternDetector, 
        use_list=False
    ) -> (float, float, float):

    true_positives: int = 0
    false_positives: int = 0
    false_negatives: int = 0

    detected: bool = False

    for key, value in ground_truth.items():
        input_file: TextIOWrapper = open(get_file_path(key))

        if use_list:
            detected = (len(detector(input_file).detect_pattern()) != 0)
        else:
            detected = detector(input_file).detect_pattern()

        if value == detected:
            true_positives += 1

        if not value and detected:
            false_positives += 1

        if value and not detected: 
            false_negatives += 1

    return calculate_metrics(true_positives, false_positives, false_negatives)


if __name__ == '__main__':
    print(all_metrics())