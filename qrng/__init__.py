"""
QRNG - Quantum Random Number Generator using Qiskit
===================================================
A reliable, Qiskit 1.x compatible true random number generation suite based on
quantum superposition, projective measurement, and NIST statistical verification.
"""

from .generator import QuantumRNG
from .statistical_tests import NISTMonobitTest, NISTRunsTest, ChiSquareUniformityTest

__version__ = "1.0.0"
__all__ = ["QuantumRNG", "NISTMonobitTest", "NISTRunsTest", "ChiSquareUniformityTest"]
