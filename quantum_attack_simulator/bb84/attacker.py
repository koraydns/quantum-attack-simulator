"""
Quantum Attack Simulator - Attacker Module
------------------------------------------
This module is part of the Quantum Attack Simulator project, licensed under the Apache 2.0 License.
It provides implementations for simulating potential attacks in the BB84 quantum key distribution protocol.

Original Repository: https://github.com/koraydns/quantum-attack-simulator
License: Apache 2.0 (See LICENSE file for details)

Note:
This module is designed for educational and research purposes. If you modify this file, 
please indicate that changes have been made and retain this notice.

For more details, visit the GitHub repository:
https://github.com/koraydns/quantum-attack-simulator
"""

from qiskit import QuantumCircuit
import random

def simulate_pns_attack(encoded_qubits, sender_intensities):
    """
    Simulate a Photon Number Splitting (PNS) attack on the qubits.

    Args:
        encoded_qubits (list): Quantum circuits representing the qubits.
        sender_intensities (list): Intensities assigned by the sender to the qubits.

    Returns:
        tuple: Forwarded qubits, intercepted qubits by attacker, and modified intensities.
    """
    attacker_intercepted = {}
    forwarded_qubits = []
    modified_intensities = []

    for i, (qubit, intensity) in enumerate(zip(encoded_qubits, sender_intensities)):
        if random.random() > 0.2:  # Attacker intercepts with 20% probability
            attacker_intercepted[i] = qubit
            modified_intensity = "lower" if intensity == "low" else "low"
        else:
            modified_intensity = intensity

        forwarded_qubits.append(qubit)
        modified_intensities.append(modified_intensity)

    return forwarded_qubits, attacker_intercepted, modified_intensities




