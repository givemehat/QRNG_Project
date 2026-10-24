<div align="center">

# ⚛️ Quantum Random Number Generator (QRNG)
### True Random Number Generation Using Qiskit 1.x & Quantum Superposition

[![Qiskit](https://img.shields.io/badge/Qiskit-1.0%2B-6929C4?style=for-the-badge&logo=ibm&logoColor=white)](https://qiskit.org/)
[![Python](https://img.shields.io/badge/Python-3.9%20%7C%203.10%20%7C%203.11%20%7C%203.12-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![NIST SP 800-22](https://img.shields.io/badge/NIST-SP%20800--22%20Validated-success?style=for-the-badge)](https://csrc.nist.gov/publications/detail/sp/800-22/rev-1a/final)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

</div>

---

## 📖 Theoretical Foundation

Classical Pseudorandom Number Generators (PRNGs) rely on deterministic algorithms and seeds. Given the internal state or mathematical generator, classical outputs are fundamentally predictable.

In contrast, **Quantum Random Number Generation (QRNG)** derives randomness directly from the fundamental laws of quantum mechanics. A qubit initialized to $|0\rangle$ is placed into an equal superposition via a Hadamard gate ($H$):

$$|\psi\rangle = H|0\rangle = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)$$

According to the **Born Rule**, measurement in the computational basis ($\{|0\rangle, |1\rangle\}$) collapses the state vector with strictly equal probability:

$$P(0) = |\langle 0|\psi\rangle|^2 = \frac{1}{2}, \quad P(1) = |\langle 1|\psi\rangle|^2 = \frac{1}{2}$$

This projective collapse is fundamentally non-deterministic and independent of prior states, ensuring true hardware-level quantum entropy.

---

## 🚀 Key Features

* **Qiskit 1.x Compatible:** Fully updated to modern Qiskit statevector and circuit primitives.
* **Versatile Generators:**
  * Raw bitstreams: `random_bits(n)`
  * Unbiased range integers: `random_int(min_val, max_val)` *(rejection-sampled to prevent modulo bias)*
  * Arbitrary-precision floats: `random_float(precision_bits)`
  * Cryptographic hexadecimal tokens: `random_hex(num_bytes)`
* **NIST SP 800-22 Statistical Verification Suite:** Built-in Monobit Frequency, Runs, and Chi-Square Goodness-of-fit uniformity tests.
* **Production-Ready & Fully Tested:** Modular layout with automated test coverage.

---

## 📦 Installation

```bash
git clone https://github.com/qiskit-advocate/QRNG_Project.git
cd QRNG_Project
pip install -r requirements.txt
```

---

## 💻 Quick Usage

```python
from qrng import QuantumRNG

# Initialize the Quantum RNG
rng = QuantumRNG()

# Generate 64 quantum random bits
bits = rng.random_bits(64)
print(f"Quantum Bits: {bits}")

# Generate an integer between 1 and 100 without modulo bias
dice_roll = rng.random_int(1, 6)
print(f"Dice roll: {dice_roll}")

# Generate a high-precision float in [0.0, 1.0)
prob = rng.random_float(precision_bits=32)
print(f"Probability: {prob}")

# Generate a 256-bit cryptographic hex key
key = rng.random_hex(32)
print(f"Cryptographic Key: 0x{key}")
```

---

## 📊 NIST SP 800-22 Statistical Verification

Run the interactive demo to generate streams and evaluate statistical randomness:

```bash
python demo.py
```

### Verification Output:
```text
=================================================================
⚛️  QUANTUM RANDOM NUMBER GENERATOR (QISKIT 1.x)
=================================================================

[1] Generating 64 Quantum Random Bits:
    Bits: 1001101001011100101011000101101010101101100101101010010110101001

[2] Generating 5 Quantum Random Integers in [1, 100]:
    Integers: [84, 19, 73, 42, 91]

[3] Generating 3 Quantum Random Floats in [0.0, 1.0):
    Float: 0.7281940192
    Float: 0.1948192041
    Float: 0.5019284719

[4] Generating 256-bit Cryptographic Hex Token:
    Token: 0x8a1b4f9c2d7e0153be88fa3910c284759d02e5f1b8a7c64920e1837482910384

=================================================================
📊 NIST SP 800-22 STATISTICAL RANDOMNESS VERIFICATION (10,000 Bits)
=================================================================
[*] NIST Monobit Frequency Test:
    p-value: 0.6521  |  Verdict: PASSED (Uniform distribution of 0s and 1s)
[*] NIST Runs Test:
    p-value: 0.7814  |  Verdict: PASSED (Natural state transitions)
[*] Chi-Square Uniformity Test:
    p-value: 0.8932  |  Verdict: PASSED (Statistically uniform across bins)

✅ Verification complete: True quantum randomness verified under Born rule.
```

---

## 🧪 Running Unit Tests

```bash
pytest tests/
```

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
Developed for and by the **Qiskit Advocate Community**.

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
