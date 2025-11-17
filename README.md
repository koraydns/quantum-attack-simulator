# Quantum Attack Simulator

A Python-based simulator for analyzing the security of quantum communication systems. In version 1.0, the simulator is focused only on the BB84 protocol. This simulator includes features to simulate and analyze the effects of **depolarization noise**, **Man-in-the-Middle (MITM) attacks**, and **Photon Number Splitting (PNS) attacks**.

## Introduction

The **Quantum Attack Simulator** allows users to study how various noise sources and attack vectors impact the security of the BB84 quantum key distribution protocol. By providing visualization tools and detailed analysis of attack effects, this simulator is an educational and research-oriented tool for understanding quantum communication vulnerabilities.

## Theoretical Background

For a comprehensive understanding of the theoretical aspects of the quantum communication and the attack scenarios simulated in this project, refer to the detailed article on [Quantum Attack Simulator](https://doi.org/10.5281/zenodo.17586868).

The post covers:
- The foundational principles of quantum cryptography.
- An in-depth explanation of the BB84 protocol.
- How depolarization noise, Man-in-the-Middle attacks, and Photon Number Splitting attacks affect quantum key distribution.
- Practical use cases and insights from the simulation.

Explore the post to gain a deeper theoretical perspective that complements the hands-on simulations provided by this repository.


## How to Use the Simulator

### Prerequisites
- **Python 3.7 or later**. The project was developed and tested in a **Python 3.11 environment**. It is recommended to use Python 3.11 to ensure compatibility and avoid potential issues. 
- Install required dependencies:
```bash
pip install -r requirements.txt
```
### Installation
Clone this repository and install locally:
 ```bash
git clone https://github.com/koraydns/quantum-attack-simulator.git 
cd quantum-attack-simulator
```
Alternatively, install the package directly via pip:
```bash
pip install quantum-attack-simulator
```
### Note for Git Clone Users
If you cloned this repository using `git clone` instead of installing via `pip`, 
you need to ensure the project directory is added to your Python path. 

Uncomment and include the following code block at the beginning of bb84_example script:

```python
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.join(current_dir, '..')
sys.path.append(project_root)
```
### Running the Simulator
To run the simulator with default settings:
```bash
python examples/bb84_example.py
```
or
```bash
quantum-sim
```
You can customize the simulation with the following arguments:

- `--attack-type`: Specify the type of attack to simulate. Options are:
  - `None (Default)`: No attack is simulated.
  - `MITM`: Simulate a Man-in-the-Middle attack.
  - `PNS`: Simulate a Photon Number Splitting attack.

- `--depolarization-noise`: Enable or disable depolarization noise.
  - `0 (Default)`: Disable depolarization noise.
  - `1`: Enable depolarization noise (with a probability of 0.1).

Examples:
```bash
quantum-sim --attack-type MITM --depolarization-noise 1
```
```bash
python examples/bb84_example.py --attack-type PNS
```
```bash
python examples/bb84_example.py --depolarization-noise 1
```

## Example Outputs and Visualizations
### Scenario 1: Depolarization Noise Enabled, No Attack

This scenario demonstrates the BB84 protocol simulation with depolarization noise applied but no attack (e.g., MITM or PNS).

#### Depolarization Noise:
- A probability of 10% is applied, meaning qubits might undergo depolarization, simulating real-world noise in the quantum channel.
- Observed mismatches in the key agreement phase are analyzed to determine whether they fall within the expected noise threshold.

#### Key Agreement:
- Despite some mismatches caused by noise, the protocol determines that the observed error rate is within the acceptable threshold for depolarization noise.
- Communication proceeds successfully, and a shared key is generated.

#### Security Checks:
- The mismatch rate is compared against the expected noise threshold. It is highly likely that no attack will be detected.
- The error rates for different intensity levels are analyzed. All rates are within the noise threshold, confirming no PNS attack.
```bash
python examples/bb84_example.py --depolarization-noise 1
```
```bash
Sender's Bits: 0000110101000111000101110111110101001100
Sender's States: DSDSDSDDSDSDSSDSDDSSSDDSSDSSDSDSDSDSDDSS
Sender's Bases: ZXZZXZZZXZXXZZZXXXXXXZZXXZXXZXZXXXZXZXXZ
Sender's Intensities: ['high', 'none', 'medium', 'none', 'high', 'none', 'medium', 'high', 'none', 'medium', 'none', 'medium', 'none', 'none', 'low', 'none', 'medium', 'low', 'none', 'none', 'none', 'low', 'low', 'none', 'none', 'low', 'none', 'none', 'medium', 'none', 'high', 'none', 'medium', 'none', 'high', 'none', 'high', 'low', 'none', 'none']


Applying depolarization noise with probability 0.1


Receiver's Bases: ZXZZXXXXZZXZXZZXZXZZZZXZXXXXZXXZXXXZZZXX
Receiver's Bits: 1001111011000111000001010111111101101100

Performing security checks...
An interception detected. Mismatched bits: 2
Mismatch detected! Analyzing possible causes...
Observed error rate: 9.52% (expected <= 10.00%)
Differences are likely caused by depolarization noise.
Communication can proceed despite mismatches caused by depolarization noise.
Error rates by intensity (for PNS Check): {'low': 0.0, 'medium': 0.0, 'high': 0.0}

Key: 000011011101011110110
The key is 21 bits long.
```
### Scenario 2: No Depolarization Noise, No Attack

This scenario represents the ideal condition where there is neither noise nor any attack on the quantum communication channel.

#### Clean Channel:
- No depolarization noise is applied, ensuring a clean quantum channel.
- Sender and receiver's bases align perfectly in the shared indices, resulting in no mismatches.

#### Key Agreement:
- A perfect match between sender and receiver bits leads to a flawless key agreement.
- The generated key is identical for both parties without any discrepancies.

#### Security Checks:
- Since there are no mismatches, it is confirmed that no interception (e.g., MITM attack) is detected.
- The absence of error rates for intensity levels confirms that no PNS attack occurred.
```bash
python examples/bb84_example.py
```
```bash
Sender's Bits: 1110010101010111111000010111011010000111
Sender's States: SDSDSDSSSSSSSDDDDDSDSSSSSSSSSSSSDDDDSSDD
Sender's Bases: ZXXXZXZZZXXZXXZZXZZXZZZZZXZZXZXXXZZXXXZX
Sender's Intensities: ['none', 'high', 'none', 'medium', 'none', 'high', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'high', 'high', 'low', 'high', 'low', 'none', 'high', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'low', 'high', 'medium', 'low', 'none', 'none', 'low', 'high']

No depolarization noise applied.

Receiver's Bases: XXZZXZZZZXXZZZXZZXXXZZXXXXZZZXXXXXXZZXXZ
Receiver's Bits: 1101100101011011000000110111111010001110

Performing security checks...
Seems no interception. The tested bits of Sender and Receiver are the same.
No significant mismatches detected. Proceeding with PNS attack detection...
Error rates by intensity (for PNS Check): {'low': 0.0, 'high': 0.0}

Key: 101010110001111011
The key is 18 bits long.
```
### Scenario 3: PNS Attack Enabled
```bash
python examples/bb84_example.py --attack-type PNS
```
```bash
Receiver's Bases: ZXXZZXXZZZZXZXXZXXZXXZZZXXXZZZXXXXZZXZZZ
Receiver's Bits: 0011010101110111010100001101001110010010

Proceeding with PNS attack detection...
Error rates by intensity (for PNS Check): {'low': 0.6, 'medium': 1.0, 'high': 0.75}
Possible PNS attack detected. Final error rate: 0.6
Communication is terminated due to possible PNS attack.
```
#### PNS Attack Visualization
- **Blue Bars:** Error rates for different intensity levels (`low`, `medium`, `high`).
- **Red Dashed Line:** Observed error rate across all qubits during communication.
- **Green Dashed Line:** Expected noise level, representing the depolarization noise threshold.

This visualization helps distinguish between natural noise and potential attacks by comparing observed error rates against expected thresholds.

![PNS Attack Effects Visualization](https://github.com/koraydns/quantum-attack-simulator/blob/e02a636fdbc347b2b56b8a8a6c397941e88dc50f/Screen_Shots/pns-attack-effects-visualization.png)

### Scenario 4: MITM Attack Enabled
```bash
python examples/bb84_example.py --attack-type MITM
```
```bash
Receiver's Bases: XXXZXZXZXZXXZXZZZXXZZXXZZXZZZZZZZZZXXZZZ
Receiver's Bits: 1000001111110010110000110111010111100100

Performing security checks...
An interception detected. Mismatched bits: 9
Mismatch detected! Analyzing possible causes...
Observed error rate: 36.00% (expected <= 10.00%)
Differences exceed depolarization noise levels and may indicate an attack.
Communication is terminated due to detected interception. Possible MITM attack.
```
#### MITM Attack Visualization
- **Orange Bar:** Mismatch rate between the Sender's and Receiver's shared bits.
- **Green Dashed Line:** Depolarization noise threshold, indicating the maximum expected error rate due to natural noise.

This visualization aids in identifying potential MITM attacks by comparing mismatch rates against the expected noise threshold.

![MITM Attack Effects Visualization](https://github.com/koraydns/quantum-attack-simulator/blob/e02a636fdbc347b2b56b8a8a6c397941e88dc50f/Screen_Shots/mitm-attack-effects-visualization.png) 

## License

This project is licensed under the Apache License, Version 2.0.  
You may obtain a copy of the License at:  [http://www.apache.org/licenses/LICENSE-2.0](http://www.apache.org/licenses/LICENSE-2.0)

Unless required by applicable law or agreed to in writing, this software is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
For more details, refer to the [LICENSE file in this repository](https://github.com/koraydns/quantum-attack-simulator/blob/main/LICENSE).
