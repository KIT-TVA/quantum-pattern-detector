# Quantum Pattern Detector

This repository contains the implementation for the paper "Quantum Pattern Detection: Accurate State- and Circuit-based Analyses".
It consists of severeal individual algorithms for detecting different [patterns for quantum computing](https://quantumcomputingpatterns.org/#/) automatically.

## Usage

In order to use this framwork, make sure to have all necessary libraires installed that are listed in the [requirements](requirements.txt).

Follow the following steps for the reproduction of the evluation results:
1. Clone this repository using
   ```
   git clone https://github.com/KIT-TVA/quantum-pattern-detector.git
   ```
2. Navigate into the `evaluation` directory inside a terminal.
3. Run either
   ```
   python -u "test.py"
   ```
   for evaluating the accuracy of our detection programs (this may take a while) or
   ```
   python scalability_test.py <argv>
   ```
   for evaluating the scalability of our detection programs.
   
   The argument `argv` is set depending on which pattern is to be evaluated and has to be one of the following values:
   - `UniformSuperposition`
   - `CreatingEntanglement`
   - `BasisEncoding`
   - `AngleEncoding`
   - `AmplitudeEncoding`
   - `QuantumPhaseEstimation`
   - `Uncompute`
   - `PostSelectiveMeasurement`

## Citation

When publishing articles or otherwise writing about this work, please cite the following:

```bibtex
@INPROCEEDINGS{11029468,
  author={Shen, Julian and Ammermann, Joshua and König, Christoph and Schaefer, Ina},
  booktitle={2025 IEEE/ACM International Workshop on Quantum Software Engineering (Q-SE)}, 
  title={Quantum Pattern Detection: Accurate State- and Circuit-Based Analyses}, 
  year={2025},
  volume={},
  number={},
  pages={9-16},
  keywords={Computers;Quantum computing;Accuracy;Codes;Source coding;Conferences;Quantum mechanics;Programming;Software;Software engineering;Quantum Computing Patterns;Quantum Software Engineering;Pattern Detection;Quantum Computing},
  doi={10.1109/Q-SE66736.2025.00008}}
```
