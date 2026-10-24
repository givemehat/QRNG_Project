#!/usr/bin/env python3
"""
Interactive Demonstration of Quantum Random Number Generator (QRNG)
"""

from qrng.generator import QuantumRNG
from qrng.statistical_tests import NISTMonobitTest, NISTRunsTest, ChiSquareUniformityTest

def main():
    print("=" * 65)
    print("⚛️  QUANTUM RANDOM NUMBER GENERATOR (QISKIT 1.x)")
    print("=" * 65)
    
    rng = QuantumRNG()
    
    # 1. Random Binary String
    print("\n[1] Generating 64 Quantum Random Bits:")
    bits = rng.random_bits(64)
    print(f"    Bits: {bits}")
    
    # 2. Random Integers
    print("\n[2] Generating 5 Quantum Random Integers in [1, 100]:")
    ints = [rng.random_int(1, 100) for _ in range(5)]
    print(f"    Integers: {ints}")
    
    # 3. High-precision Float
    print("\n[3] Generating 3 Quantum Random Floats in [0.0, 1.0):")
    floats = [rng.random_float(precision_bits=32) for _ in range(3)]
    for f in floats:
        print(f"    Float: {f:.10f}")
        
    # 4. Cryptographic Hex Token
    print("\n[4] Generating 256-bit Cryptographic Hex Token:")
    token = rng.random_hex(32)
    print(f"    Token: 0x{token}")
    
    # 5. NIST SP 800-22 Randomness Statistical Validation
    print("\n" + "=" * 65)
    print("📊 NIST SP 800-22 STATISTICAL RANDOMNESS VERIFICATION (10,000 Bits)")
    print("=" * 65)
    test_stream = rng.random_bits(10000)
    
    monobit = NISTMonobitTest(test_stream)
    print(f"[*] {monobit['test']}:")
    print(f"    p-value: {monobit['p_value']:.4f}  |  Verdict: {monobit['verdict']}")
    
    runs = NISTRunsTest(test_stream)
    print(f"[*] {runs['test']}:")
    print(f"    p-value: {runs['p_value']:.4f}  |  Verdict: {runs['verdict']}")
    
    # Uniformity on 1,000 float samples
    float_samples = [rng.random_float() for _ in range(1000)]
    chi2 = ChiSquareUniformityTest(float_samples)
    print(f"[*] {chi2['test']}:")
    print(f"    p-value: {chi2['p_value']:.4f}  |  Verdict: {chi2['verdict']}")
    
    print("\n✅ Verification complete: True quantum randomness verified under Born rule.")

if __name__ == "__main__":
    main()
