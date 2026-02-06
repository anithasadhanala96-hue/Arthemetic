"""
Tests for naturalnosum.py

Based on the function name 'naturalnumbersum' and file name 'naturalnosum.py':
This script should compute the sum of the first N natural numbers.
Expected formula: N * (N + 1) / 2
CLI args: n (the count of natural numbers to sum)
"""

import pytest


class TestNaturalNumberSum:

    def test_sum_of_first_1(self, run_script):
        """Sum of first 1 natural number = 1."""
        result = run_script("naturalnosum.py", ["1"])
        assert result.returncode == 0
        assert float(result.stdout.strip()) == pytest.approx(1.0)

    def test_sum_of_first_5(self, run_script):
        """Sum of 1+2+3+4+5 = 15."""
        result = run_script("naturalnosum.py", ["5"])
        assert result.returncode == 0
        assert float(result.stdout.strip()) == pytest.approx(15.0)

    def test_sum_of_first_10(self, run_script):
        """Sum of 1..10 = 55."""
        result = run_script("naturalnosum.py", ["10"])
        assert result.returncode == 0
        assert float(result.stdout.strip()) == pytest.approx(55.0)

    def test_sum_of_first_100(self, run_script):
        """Sum of 1..100 = 5050."""
        result = run_script("naturalnosum.py", ["100"])
        assert result.returncode == 0
        assert float(result.stdout.strip()) == pytest.approx(5050.0)

    def test_sum_of_zero(self, run_script):
        """Sum of first 0 natural numbers should be 0."""
        result = run_script("naturalnosum.py", ["0"])
        assert result.returncode == 0
        assert float(result.stdout.strip()) == pytest.approx(0.0)

    def test_sum_large_number(self, run_script):
        """Sum of 1..1000 = 500500."""
        result = run_script("naturalnosum.py", ["1000"])
        assert result.returncode == 0
        assert float(result.stdout.strip()) == pytest.approx(500500.0)

    def test_missing_arg_fails(self, run_script):
        """Running with no argument should fail."""
        result = run_script("naturalnosum.py", [])
        assert result.returncode != 0
