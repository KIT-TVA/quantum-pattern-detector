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
