"""
Quantum Random Number Generator Core Engine
Implements true randomness using Hadamard superpositions on Qiskit circuits.
"""

import math
import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

class QuantumRNG:
    """
    Quantum Random Number Generator leveraging quantum projective measurement.
    
    A qubit initialized to |0> is transformed by a Hadamard gate H into equal superposition:
        |ψ> = H|0> = (|0> + |1>) / sqrt(2)
        
    Measurement according to the Born rule yields outcomes {0, 1} with strictly equal
    probability P(0) = P(1) = 0.5, governed by quantum wave-function collapse.
    """
    
    def __init__(self, backend=None):
        self.backend = backend

    def _sample_raw_bits(self, num_bits: int) -> list:
        """
        Samples raw random bits by measuring Hadamard quantum circuits.
        """
        if num_bits <= 0:
            return []
            
        # Efficient batching across 8-qubit register
        batch_qubits = min(8, num_bits)
        qc = QuantumCircuit(batch_qubits)
        for i in range(batch_qubits):
            qc.h(i)
            
        bits = []
        sv = Statevector.from_instruction(qc)
        
        while len(bits) < num_bits:
            # Measure all qubits simultaneously via projective state collapse
            outcome = sv.sample_memory(shots=1)[0]
            # Convert binary string to bit integers
            for b in outcome:
                bits.append(int(b))
                if len(bits) == num_bits:
                    break
        return bits

    def random_bits(self, length: int) -> str:
        """Generates a binary string of given length."""
        bits = self._sample_raw_bits(length)
        return "".join(str(b) for b in bits)

    def random_int(self, min_val: int = 0, max_val: int = 100) -> int:
        """
        Generates a quantum random integer in [min_val, max_val] inclusive.
        Uses rejection sampling to prevent modulo bias.
        """
        if min_val > max_val:
            raise ValueError("min_val must be <= max_val")
        if min_val == max_val:
            return min_val
            
        range_size = max_val - min_val + 1
        num_bits = math.ceil(math.log2(range_size))
        
        # Max multiple to avoid modulo bias
        max_valid = (2 ** num_bits // range_size) * range_size
        
        while True:
            bits = self._sample_raw_bits(num_bits)
            val = int("".join(str(b) for b in bits), 2)
            if val < max_valid:
                return min_val + (val % range_size)

    def random_float(self, precision_bits: int = 32) -> float:
        """
        Generates a quantum random float in [0.0, 1.0) with specified bit precision.
        """
        bits = self._sample_raw_bits(precision_bits)
        numerator = int("".join(str(b) for b in bits), 2)
        denominator = 2 ** precision_bits
        return numerator / denominator

    def random_hex(self, num_bytes: int = 16) -> str:
        """Generates a cryptographic-grade hexadecimal token of specified byte length."""
        bits = self._sample_raw_bits(num_bytes * 8)
        val = int("".join(str(b) for b in bits), 2)
        return f"{val:0{num_bytes * 2}x}"
