"""
Quantum Attack Simulator - Sender Module
----------------------------------------
This module is part of the Quantum Attack Simulator project, licensed under the Apache 2.0 License.
It implements the sender's actions in the BB84 quantum key distribution protocol, including:

- Generating random bits and states.
- Encoding qubits based on the selected bases.
- Assigning intensities to qubits.
- Sending encoded qubits over a quantum channel.

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

def generate_random_bits_for_sender(key_length):
    """
    Generate a random string of bits to be sent by the sender along with their states.

    Args:
        key_length (int): The length of the key to generate.

    Returns:
        tuple: 
            - sender_bits (str): Randomly generated bits ('0' or '1') for the sender.
            - state_of_bits (str): Corresponding states of each bit ('S' for Signal, 'D' for Decoy).
    """
    sender_bits = ""
    state_of_bits = ""
    states = ["S", "D"]  # S: Signal State, D: Decoy State

    for _ in range(key_length):
        rand_bit = random.randint(0, 1)  # Randomly choose the bit
        sender_bits += str(rand_bit)  # Add randomly chosen bit to the bit string
        bit_state = random.choice(states)  # Randomly choose the state of bit
        state_of_bits += bit_state  # Add randomly chosen state to the states string

    return sender_bits, state_of_bits


def generate_random_intensities(num_of_qubits, qubits_states):
    """
    Assign random intensities to decoy qubits based on their states.

    Parameters:
        num_of_qubits (int): Number of qubits to generate intensities for.
        qubits_states (str): States of the qubits ('S' for signal, 'D' for decoy).

    Returns:
        list: Intensities assigned to each qubit ('low', 'medium', 'high', or 'none').
    """
    intensities = []
    for i in range(num_of_qubits):
        if qubits_states[i] == "D":
            intensity = random.choice(["low", "medium", "high"])
            intensities.append(intensity)  # If qubit is decoy, assign intensity
        else:
            intensities.append("none")  # Signal qubit has no intensity
    return intensities


def select_random_bases(num_bases):
    """
    Randomly select bases ('Z' or 'X') for quantum state preparation or measurement.

    Parameters:
        num_bases (int): Number of bases to generate.

    Returns:
        str: A string of randomly chosen bases ('Z' or 'X').
    """
    bases_string = ""
    for i in range(num_bases):
        rand_basis = random.randint(0, 1)
        bases_string += "Z" if rand_basis == 0 else "X"
    return bases_string


def encode_quantum_bits(bits, bases):
    """
    Transform classical bits into quantum representations based on provided bases.

    This function uses classical bits and encoding bases to prepare quantum states.
    The encoding process varies depending on the basis:
    - 'Z' basis creates standard quantum states (|0> and |1>).
    - 'X' basis prepares superposition states (|+> and |->).

    Parameters:
        bits (str): A binary string representing the classical bits (e.g., "0101").
        bases (str): A string specifying the bases ('Z' or 'X') for encoding.

    Returns:
        list: A list of QuantumCircuit objects, each representing a quantum state.
    """
    encoded_qubits = []
    actions = {
        ("0", "Z"): [],
        ("1", "Z"): ["x"],
        ("0", "X"): ["h"],
        ("1", "X"): ["x", "h"]
    }

    for bit, basis in zip(bits, bases):
        qc = QuantumCircuit(1, 1) 
        for action in actions[(bit, basis)]:
            getattr(qc, action)(0)
        encoded_qubits.append(qc)

    return encoded_qubits