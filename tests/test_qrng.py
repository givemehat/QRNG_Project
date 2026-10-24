"""
Unit Tests for Quantum Random Number Generator (QRNG)
"""

import unittest
from qrng.generator import QuantumRNG
from qrng.statistical_tests import NISTMonobitTest, NISTRunsTest, ChiSquareUniformityTest

class TestQuantumRNG(unittest.TestCase):
    def setUp(self):
        self.rng = QuantumRNG()

    def test_random_bits(self):
        bits = self.rng.random_bits(128)
        self.assertEqual(len(bits), 128)
        self.assertTrue(set(bits).issubset({'0', '1'}))

    def test_random_int_bounds(self):
        for _ in range(50):
            val = self.rng.random_int(10, 20)
            self.assertTrue(10 <= val <= 20)

    def test_random_int_single_value(self):
        self.assertEqual(self.rng.random_int(5, 5), 5)

    def test_random_float_bounds(self):
        for _ in range(50):
            val = self.rng.random_float(16)
            self.assertTrue(0.0 <= val < 1.0)

    def test_random_hex(self):
        token = self.rng.random_hex(16)
        self.assertEqual(len(token), 32)
        int(token, 16)  # Valid hex integer

    def test_nist_monobit(self):
        bits = self.rng.random_bits(2000)
        res = NISTMonobitTest(bits)
        self.assertTrue(res["passed"])

    def test_nist_runs(self):
        bits = self.rng.random_bits(2000)
        res = NISTRunsTest(bits)
        self.assertTrue(res["passed"])

if __name__ == "__main__":
    unittest.main()
