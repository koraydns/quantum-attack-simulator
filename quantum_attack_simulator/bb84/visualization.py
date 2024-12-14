"""
Quantum Attack Simulator - Visualization Module
-----------------------------------------------
This module is part of the Quantum Attack Simulator project, licensed under the Apache 2.0 License.
It provides tools for visualizing the results of the BB84 quantum key distribution protocol, including:

- Visualizing error rates by intensity levels.
- Analyzing the impact of Photon Number Splitting (PNS) attacks.
- Highlighting mismatches and error thresholds due to depolarization noise or interception.
- Generating clear and interpretable charts to support security analysis.

Original Repository: https://github.com/koraydns/quantum-attack-simulator
License: Apache 2.0 (See LICENSE file for details)

Note:
This module is designed for educational and research purposes. If you modify this file, 
please indicate that changes have been made and retain this notice.

For more details, visit the GitHub repository:
https://github.com/koraydns/quantum-attack-simulator
"""

import matplotlib.pyplot as plt

def visualize_pns_results(error_rates, observed_error_rate, noise_probability):
    """
    Visualize error rates and observed error rate against the depolarization noise level.

    Parameters:
        error_rates (dict): Error rates for each intensity level.
        observed_error_rate (float): Observed error rate between Sender and Receiver.
        noise_probability (float): Expected depolarization noise probability.
    """
    if observed_error_rate is None:
        print("Error: Observed error rate is None. Visualization skipped.")
        return

    # Plot error rates for different intensities
    intensities = list(error_rates.keys())
    rates = list(error_rates.values())

    plt.figure(figsize=(10, 6))
    plt.bar(intensities, rates, label="Error Rates by Intensity", alpha=0.7, color="blue")

    # Add observed error rate as a horizontal line
    plt.axhline(y=observed_error_rate, color="red", linestyle="--", label="Observed Error Rate")
    plt.axhline(y=noise_probability, color="green", linestyle="--", label="Expected Noise Level")

    plt.title("Error Rate Analysis for PNS Attack Detection")
    plt.xlabel("Intensity Levels")
    plt.ylabel("Error Rate")
    plt.legend()
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()

def visualize_mitm_results(mismatch_count, total_bits, depolarization_threshold):
    """
    Visualize the mismatch rate in comparison to the depolarization noise threshold.

    Parameters:
        mismatch_count (int): Number of mismatched bits between Sender and Receiver.
        total_bits (int): Total number of bits compared between Sender and Receiver.
        depolarization_threshold (float): Expected maximum error rate caused by depolarization noise.
    """
    # Calculate mismatch rate
    mismatch_rate = mismatch_count / total_bits

    plt.figure(figsize=(8, 5))
    plt.bar(["Mismatch Rate"], [mismatch_rate], color="orange", label="Mismatch Rate")
    plt.axhline(y=depolarization_threshold, color="green", linestyle="--", label="Depolarization Threshold")

    plt.title("Mismatch Analysis for MITM Detection")
    plt.ylabel("Rate")
    plt.ylim(0, max(mismatch_rate, depolarization_threshold) + 0.05)  # Adjust y-axis range dynamically
    plt.legend()
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()
