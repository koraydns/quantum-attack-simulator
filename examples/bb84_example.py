"""
Quantum Attack Simulator
------------------------
Original Repository: https://github.com/koraydns/quantum-attack-simulator
Author: Koray Danisma

License: Apache 2.0
This project is licensed under the Apache License 2.0.
For full license details, see the LICENSE file in the repository.

Note:
If you modify this file, you must indicate that changes have been made.
"""

"""
BB84 Protocol Security Simulation Script

This script focuses on the security aspects of the BB84 quantum key distribution protocol
using the Quantum Attack Simulator library. It simulates potential attacks and evaluates
the robustness of quantum communication against these threats. The script includes:

1. Random Bit and Qubit Generation:
   The sender generates random bits, states, and bases.

2. Attack and Noise Simulation:
   - Depolarization Noise: Simulates natural noise in quantum communication (optional).
   - MITM (Man-in-the-Middle) Attack: Simulates an attacker intercepting and altering qubits (optional).
   - PNS (Photon Number Splitting) Attack: Simulates an attacker selectively intercepting qubits based on photon intensities (optional).

3. Measurement and Key Agreement:
   The receiver measures qubits and performs key reconciliation with the sender.

4. Security Checks:
   Detects potential interception (MITM) and analyzes if mismatches are caused by depolarization noise.
   Detects potential PNS attacks using error rate analysis.

5. Key Generation:
   If no attacks are detected, the final key is generated.

6. Visualization:
   Includes visualizations of error rates and attack impacts.

Usage:
Run this script from the command line, specifying the attack type and noise settings:

python bb84_example.py --attack-type [None (Default)|MITM|PNS] --depolarization-noise [0 (Default)|1]

Arguments:
--attack-type           Specify the type of attack to simulate (None, MITM, or PNS).
--depolarization-noise  Apply depolarization noise (0 for no noise, 1 to enable).

Example:
Simulate a PNS attack with depolarization noise:

python bb84_example.py --attack-type PNS --depolarization-noise 1

For more details, visit the GitHub repository:
https://github.com/koraydns/quantum-attack-simulator
"""
import argparse
from quantum_attack_simulator.bb84 import sender, receiver, attacker, visualization
from quantum_attack_simulator.communication import apply_depolarization_noise


# Note for git clone users:
# If you use `git clone` instead of `pip install`, ensure the project directory is added to `sys.path` in your script.
# Uncomment the following code block to configure the path manually:
"""
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.join(current_dir, '..')  
sys.path.append(project_root)  
"""

def main():
    parser = argparse.ArgumentParser(
        description=(
            "Quantum Key Distribution Simulation with BB84 Protocol. "
            "This simulation focuses on the security of quantum communication, "
            "including the detection of potential attacks like MITM and PNS, "
            "and the effects of depolarization noise."
        )
    )

    parser.add_argument(
        "--attack-type", 
        type=str, 
        choices=["None", "MITM", "PNS"], 
        default="None",
        help="Type of attack to simulate: None, MITM, or PNS."
    )
    parser.add_argument(
        "--depolarization-noise", 
        type=int, 
        choices=[0, 1], 
        default=0,
        help="Apply depolarization noise: 0 for no noise, 1 to apply noise with probability 0.1"
    )

    args = parser.parse_args()
    attack_type = args.attack_type
    depolarization_noise = args.depolarization_noise

    KEY_LENGTH = 40  # Define the key length

    # Step 1: Sender generates random bits, states, and bases
    sender_bits, sender_states = sender.generate_random_bits_for_sender(KEY_LENGTH)
    sender_bases = sender.select_random_bases(KEY_LENGTH)
    sender_intensities = sender.generate_random_intensities(KEY_LENGTH, sender_states)
    encoded_qubits = sender.encode_quantum_bits(sender_bits, sender_bases)

    print(f"Sender's Bits: {sender_bits}")
    print(f"Sender's States: {sender_states}")
    print(f"Sender's Bases: {sender_bases}")
    print(f"Sender's Intensities: {sender_intensities}")
    print("\n")

    # Step 2: Sender sends qubits through the quantum channel
    quantum_channel = encoded_qubits

    # Step 3: Apply Depolarization Noise (Optional)
    if depolarization_noise == 1:
        print("Applying depolarization noise with probability 0.1")
        quantum_channel = apply_depolarization_noise(quantum_channel, noise_probability=0.1)
    else:
        print("No depolarization noise applied.")

    # Step 4: Simulate MITM Attack (Optional)
    if attack_type == "MITM":
        print("Simulating MITM attack...")
        attacker_bases = sender.select_random_bases(KEY_LENGTH)
        attacker_bits = receiver.measure_quantum_states(quantum_channel, attacker_bases)
        quantum_channel = sender.encode_quantum_bits(attacker_bits, attacker_bases)

    # Step 5: Simulate PNS Attack (Optional)
    if attack_type == "PNS":
        print("Simulating PNS attack...")
        quantum_channel, intercepted, modified_intensities = attacker.simulate_pns_attack(quantum_channel, sender_intensities)
        receiver_intensities = modified_intensities
    else:
        receiver_intensities = sender_intensities

    # Step 6: Receiver measures the qubits
    receiver_bases = receiver.select_random_bases(KEY_LENGTH)
    receiver_bits = receiver.measure_quantum_states(quantum_channel, receiver_bases)

    print("\n")
    print(f"Receiver's Bases: {receiver_bases}")
    print(f"Receiver's Bits: {receiver_bits}")

    # Step 7: Key Agreement and Security Checks
    common_indices = [i for i in range(KEY_LENGTH) if sender_bases[i] == receiver_bases[i]]
    sender_key_bits = [sender_bits[i] for i in common_indices]
    receiver_key_bits = [receiver_bits[i] for i in common_indices]
    sender_intensities_common = [sender_intensities[i] for i in common_indices]
    receiver_intensities_common = [receiver_intensities[i] for i in common_indices]

    # Detect MITM Attack
    print("\nPerforming security checks...")
    if receiver.detect_interception(sender_key_bits, receiver_key_bits):
        print("Mismatch detected! Analyzing possible causes...")
        if receiver.analyze_depolarization_impact(sender_key_bits, receiver_key_bits, noise_probability=0.1):
            print("Communication can proceed despite mismatches caused by depolarization noise.")
        else:
            print("Communication is terminated due to detected interception. Possible MITM attack.")
            mismatch_count = sum(1 for a, b in zip(sender_key_bits, receiver_key_bits) if a != b)
            visualization.visualize_mitm_results(mismatch_count, len(sender_key_bits), depolarization_threshold=0.1)
            return
    else:
        print("No significant mismatches detected. Proceeding with PNS attack detection...")

    # Detect PNS Attack
    error_rates = receiver.calculate_error_rates(sender_intensities_common, receiver_intensities_common)
    print("Error rates by intensity (for PNS Check):", error_rates)
    is_pns_attack, final_error = receiver.check_error_rates(error_rates)
    if is_pns_attack:
        print(f"Possible PNS attack detected. Final error rate: {final_error}")
        print("Communication is terminated due to possible PNS attack.")
        visualization.visualize_pns_results(error_rates, observed_error_rate=final_error, noise_probability=0.1)
        return

    # Generate Key
    final_key = receiver.generate_key(sender_key_bits)

if __name__ == "__main__":
    main()

