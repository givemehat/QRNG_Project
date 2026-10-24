"""
Statistical Randomness Verification Suite (NIST SP 800-22 Standard)
Evaluates generated quantum bitstreams for statistical uniformity and independence.
"""

import math
from scipy import special, stats

def NISTMonobitTest(bitstring: str) -> dict:
    """
    NIST SP 800-22 Frequency (Monobit) Test.
    Tests whether the number of ones and zeros are approximately equal.
    """
    n = len(bitstring)
    if n == 0:
        return {"passed": False, "p_value": 0.0, "reason": "Empty string"}
        
    s_n = sum(1 if b == '1' else -1 for b in bitstring)
    s_obs = abs(s_n) / math.sqrt(n)
    p_value = special.erfc(s_obs / math.sqrt(2))
    
    passed = p_value >= 0.01
    return {
        "test": "NIST Monobit Frequency Test",
        "passed": passed,
        "p_value": float(p_value),
        "statistic": float(s_obs),
        "verdict": "PASSED (Uniform distribution of 0s and 1s)" if passed else "FAILED (Skew detected)"
    }

def NISTRunsTest(bitstring: str) -> dict:
    """
    NIST SP 800-22 Runs Test.
    Tests whether oscillation between zeros and ones is too fast or too slow.
    """
    n = len(bitstring)
    ones = bitstring.count('1')
    prop = ones / n
    
    # Prerequisite check
    if abs(prop - 0.5) >= (2 / math.sqrt(n)):
        return {
            "test": "NIST Runs Test",
            "passed": False,
            "p_value": 0.0,
            "verdict": "FAILED (Frequency prerequisite failed)"
        }
        
    v_obs = 1
    for i in range(n - 1):
        if bitstring[i] != bitstring[i + 1]:
            v_obs += 1
            
    numerator = abs(v_obs - (2 * n * prop * (1 - prop)))
    denominator = 2 * math.sqrt(2 * n) * prop * (1 - prop)
    p_value = special.erfc(numerator / denominator)
    
    passed = p_value >= 0.01
    return {
        "test": "NIST Runs Test",
        "passed": passed,
        "p_value": float(p_value),
        "v_obs": v_obs,
        "verdict": "PASSED (Natural state transitions)" if passed else "FAILED (Run length anomaly)"
    }

def ChiSquareUniformityTest(samples: list, num_bins: int = 10) -> dict:
    """
    Pearson's Chi-Square Goodness-of-Fit Test for uniform sample distributions.
    """
    observed, _ = [list(x) for x in (None, None)] if False else (None, None)
    import numpy as np
    observed, _ = np.histogram(samples, bins=num_bins)
    expected = [len(samples) / num_bins] * num_bins
    chi2_stat, p_value = stats.chisquare(f_obs=observed, f_exp=expected)
    
    passed = p_value >= 0.05
    return {
        "test": "Chi-Square Uniformity Test",
        "passed": passed,
        "p_value": float(p_value),
        "chi2": float(chi2_stat),
        "verdict": "PASSED (Statistically uniform across bins)" if passed else "FAILED"
    }
