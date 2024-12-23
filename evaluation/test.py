"""Methods for evaluating the performance of the pattern detectors."""

import os, sys
parent_dir: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir + "/src")

import json

from abstract_detector import PatternDetector
from state_prep import AngleEncodingDetector, BasisEncodingDetector, AmplitudeEncodingDetector
from quantum_states import EntanglementDetector, UniformSuperpositionDetector
from unitary_transformation import PhaseEstimationDetector, UncomputeDetector
from measurement import PostSelectiveMeasurementDetector

from io import TextIOWrapper
from pathlib import Path


FILE_PATH: list[str] = ["adder_with_overflow",
                        "adder_without_overflow",
                        "amplitude_encoding",
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
    """Construct messages of all pattern detectors in a readable format.
    
    Returns: 
        str: Messages of every pattern detector.
    """
    msg: str = ""

    for file_str in FILE_PATH:
        input_file: TextIOWrapper = open(get_file_path(file_str))
        msg += file_str + ":" + "\n" + \
                "---------------------------------" + "\n" + \
                UniformSuperpositionDetector(input_file).build_message() + "\n" + \
                EntanglementDetector(input_file).build_message() + "\n" + \
                BasisEncodingDetector(input_file).build_message() + "\n" + \
                AngleEncodingDetector(input_file).build_message() + "\n" + \
                AmplitudeEncodingDetector(input_file).build_message() + "\n" + \
                PhaseEstimationDetector(input_file).build_message() + "\n" + \
                UncomputeDetector(input_file).build_message() + "\n" + \
                PostSelectiveMeasurementDetector(input_file).build_message() + "\n\n"

    return msg.strip()

def all_messages_from_path(directory_path: str) -> str:
    """Construct messages of all pattern detectors in a readable format for all OpenQASM files in a given directory.
    
    Returns: 
        str: Messages of every pattern detector.
    """
    msg: str = ""
    file_count: int = 0

    pathlist = Path(directory_path).rglob('*.qasm')

    for path in pathlist:
        input_file: TextIOWrapper = open(str(path))
        print(os.path.basename(str(path)))
        msg += os.path.basename(str(path)) + ":" + "\n" + \
            "---------------------------------" + "\n" + \
            UniformSuperpositionDetector(input_file).build_message() + "\n" + \
            EntanglementDetector(input_file).build_message() + "\n" + \
            BasisEncodingDetector(input_file).build_message() + "\n" + \
            AngleEncodingDetector(input_file).build_message() + "\n" + \
            AmplitudeEncodingDetector(input_file).build_message() + "\n" + \
            PhaseEstimationDetector(input_file).build_message() + "\n" + \
            UncomputeDetector(input_file).build_message() + "\n" + \
            PostSelectiveMeasurementDetector(input_file).build_message() + "\n\n"

        file_count += 1
        print(str(file_count) + "/" + str(68))

    return msg.strip()

def all_metrics() -> str:
    """Calculate evaluation metrics for every patten detector.
    
    The metrics precision, recall and f-measure are used for evaluation.

    Returns:
        str: The calculated evaluation metrics for every pattern detector.
    """
    return (metrics_ufs() + "\n" + \
            metrics_entanglement() + "\n" + \
            metrics_basis_encoding() + "\n" + \
            metrics_angle_encoding() + "\n" + \
            metrics_amplitude_encoding() + "\n" + \
            metrics_qpe() + "\n" + \
            metrics_uncompute() + "\n" + \
            metrics_psm()).strip()

def metrics_ufs() -> str:
    """Calculate the metrics precision, recall and f-measure for the Uniform Superposition detector.
    
    Returns:
        str: The calculated evaluation metrics for the Uniform Superposition detector.
    """
    ground_truth = load_ground_truth("ufs")
    metrics: tuple[float, float, float] = metrics_for_line_detectors(ground_truth, UniformSuperpositionDetector)

    return "Uniform superposition detector\n" + \
           "----------------------------------\n" +\
           "Precison: {p}, Recall: {r}, F-Measure: {f}\n".format(p=metrics[0], r=metrics[1], f=metrics[2])

def metrics_entanglement() -> str:
    """Calculate the metrics precision, recall and f-measure for the Creating Entanglement detector.
    
    Returns:
        str: The calculated evaluation metrics for the Creating Entanglement detector.
    """
    ground_truth = load_ground_truth("entanglement")
    metrics: tuple[float, float, float] = metrics_for_line_detectors(ground_truth, EntanglementDetector)

    return "Entanglement detector\n" + \
           "----------------------------------\n" +\
           "Precison: {p}, Recall: {r}, F-Measure: {f}\n".format(p=metrics[0], r=metrics[1], f=metrics[2])

def metrics_basis_encoding() -> str: 
    """Calculate the metrics precision, recall and f-measure for the Basis Encoding detector.
    
    Returns:
        str: The calculated evaluation metrics for the Basis Encoding detector.
    """
    ground_truth = load_ground_truth("basis_encoding")
    metrics: tuple[float, float, float] = metrics_for_instance_detectors(
                                            ground_truth, 
                                            BasisEncodingDetector, 
                                            use_list=True
                                        )

    return "Basis encoding detector\n" + \
           "----------------------------------\n" +\
           "Precison: {p}, Recall: {r}, F-Measure: {f}\n".format(p=metrics[0], r=metrics[1], f=metrics[2])

def metrics_angle_encoding() -> str: 
    """Calculate the metrics precision, recall and f-measure for the Angle Encoding detector.
    
    Returns:
        str: The calculated evaluation metrics for the Angle Encoding detector.
    """
    ground_truth = load_ground_truth("angle_encoding")
    metrics: tuple[float, float, float] = metrics_for_instance_detectors(
                                            ground_truth, 
                                            AngleEncodingDetector, 
                                            use_list=True
                                        )

    return "Angle encoding detector\n" + \
           "----------------------------------\n" +\
           "Precison: {p}, Recall: {r}, F-Measure: {f}\n".format(p=metrics[0], r=metrics[1], f=metrics[2])

def metrics_amplitude_encoding() -> str: 
    """Calculate the metrics precision, recall and f-measure for the Amplitude Encoding detector.
    
    Returns:
        str: The calculated evaluation metrics for the Amplitude Encoding detector.
    """
    ground_truth = load_ground_truth("amplitude_encoding")
    metrics: tuple[float, float, float] = metrics_for_instance_detectors(ground_truth, AmplitudeEncodingDetector)

    return "Amplitude Encoding detector\n" + \
           "----------------------------------\n" +\
           "Precison: {p}, Recall: {r}, F-Measure: {f}\n".format(p=metrics[0], r=metrics[1], f=metrics[2])

def metrics_qpe() -> str: 
    """Calculate the metrics precision, recall and f-measure for the Quantum Phase Estimation detector.
    
    Returns:
        str: The calculated evaluation metrics for the Quantum Phase Estimation detector.
    """
    ground_truth = load_ground_truth("qpe")
    metrics: tuple[float, float, float] = metrics_for_instance_detectors(ground_truth, PhaseEstimationDetector)

    return "Quantum Phase Estimation detector\n" + \
           "----------------------------------\n" +\
           "Precison: {p}, Recall: {r}, F-Measure: {f}\n".format(p=metrics[0], r=metrics[1], f=metrics[2])

def metrics_uncompute() -> str: 
    """Calculate the metrics precision, recall and f-measure for the Uncompute detector.
    
    Returns:
        str: The calculated evaluation metrics for the Uncompute detector.
    """
    ground_truth = load_ground_truth("uncompute")
    metrics: tuple[float, float, float] = metrics_for_instance_detectors(ground_truth, UncomputeDetector)

    return "Uncompute detector\n" + \
           "----------------------------------\n" +\
           "Precison: {p}, Recall: {r}, F-Measure: {f}\n".format(p=metrics[0], r=metrics[1], f=metrics[2])

def metrics_psm() -> str: 
    """Calculate the metrics precision, recall and f-measure for the Post Selective Measurement detector.
    
    Returns:
        str: The calculated evaluation metrics for the Post Selective Measurement detector.
    """
    ground_truth = load_ground_truth("psm")
    metrics: tuple[float, float, float] = metrics_for_instance_detectors(
                                            ground_truth, 
                                            PostSelectiveMeasurementDetector, 
                                            use_list=True
                                        )

    return "Post Selctive Measurement detector\n" + \
           "----------------------------------\n" +\
           "Precison: {p}, Recall: {r}, F-Measure: {f}\n".format(p=metrics[0], r=metrics[1], f=metrics[2])

def get_file_path(file_str: str) -> str:
    """Compute the path to the file with a certain name in the evaluation framework.
    
    Args:
        file_str (str): Name of the file.

    Returns:
        str: Path to the file with the name ```file_str``.
    """
    path_str: str = parent_dir + "/evaluation/"
    file_path: str = path_str + file_str + "/" + file_str + ".qasm"
    
    return file_path

def calculate_metrics(tp: int, fp: int, fn: int) -> tuple[float, float, float]:
    """Calculate the evaluation metrics for given numbers of true positives, false positives and false negatives.

    Args: 
        tp (int): Nuber of true positives.
        fp (int): Nuber of false positives.
        fn (int): Nuber of false negatives.

    Returns:
        tuple[float, float, float]: Tuple containing the values precision, recall and f-measure.
    """

    precision: float = tp / (tp + fp)
    recall: float = tp / (tp + fn)
    f_measure: float = (2 * precision * recall) / (precision + recall)

    return (round(precision, 4), round(recall, 4), round(f_measure, 4))

def metrics_for_line_detectors(
        ground_truth: dict[str, list[tuple[int, int]]], 
        detector: PatternDetector
    ) -> tuple[float, float, float]:
    """Calculate evaluation metrics for detectors which return code lines as pattern instances.
    
    These detectors are detectors for Uniform Superposition and Creating Entanglement.

    Args:
        ground_truth (dict[str, list[tuple[int, int]]]): The ground truth for an algorithm that is used for evaluation.
        detector (PatternDetector): The pattern detector to evaluate.

    Returns:
        tuple[float, float, float]: Tuple containing the values precision, recall and f-measure.
    """
    
    true_positives: int = 0
    false_positives: int = 0
    false_negatives: int = 0

    for key, value in ground_truth.items():
        input_file: TextIOWrapper = open(get_file_path(key))
        detected_instances: list[tuple[int, int]] = detector(input_file).detect_pattern()
        converted_value: list[tuple[int, int]] = [tuple(l) for l in value]

        if converted_value == detected_instances:
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
        use_list: bool = False
    ) -> tuple[float, float, float]:
    """Calculate evaluation metrics for detectors which return pattern instances without code line information.
    
    These detectors are detectors for Basis Encoding, Angle Encoding, Quantum Phase Estimation, Uncompute and 
    Post Selective Measurement.

    Args:
        ground_truth (dict[str, list[tuple[int, int]]]): The ground truth for an algorithm that is used for evaluation.
        detector (PatternDetector): The pattern detector to evaluate.
        use_list (bool): Optional. Specifies if the detector uses lists for pattern description.

    Returns:
        tuple[float, float, float]: Tuple containing the values precision, recall and f-measure.
    """

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

def load_ground_truth(metric_name: str) -> dict:
    """Loads the ground truth data for a given detector.

    Args: 
        metric_name (str): The abbreviation for the detector.

    Returns:
        dict: A dictionary containing the ground truth.
    """
    with open(parent_dir + "/evaluation/ground_truth.json") as json_data:
        ground_truth_data = json.load(json_data)
    return ground_truth_data.get(metric_name, {})


if __name__ == '__main__':
    print(all_metrics())

    # with open("C:\\quantum-pattern-detector\\evaluation\\dataset_cmp\\result.txt", "w") as result_file:
    #    result_file.write(all_messages("C:\\quantum-pattern-detector\\evaluation\\dataset_cmp"))