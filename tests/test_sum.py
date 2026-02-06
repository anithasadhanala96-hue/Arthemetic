"""
Tests for sum.py

Based on the function name 'myfunction' in file 'sum.py':
This script should compute and print the sum of 2 numbers provided as CLI args.
Expected: arg1 + arg2
"""

import pytest


class TestSum:

    def test_sum_positive_numbers(self, run_script):
        """Sum of 3 + 5 should be 8."""
        result = run_script("sum.py", ["3", "5"])
        assert result.returncode == 0
        assert int(result.stdout.strip()) == 8

    def test_sum_with_zero(self, run_script):
        """Sum of 0 + 7 should be 7."""
        result = run_script("sum.py", ["0", "7"])
        assert result.returncode == 0
        assert int(result.stdout.strip()) == 7

    def test_sum_both_zero(self, run_script):
        """Sum of 0 + 0 should be 0."""
        result = run_script("sum.py", ["0", "0"])
        assert result.returncode == 0
        assert int(result.stdout.strip()) == 0

    def test_sum_negative_numbers(self, run_script):
        """Sum of -3 + -5 should be -8."""
        result = run_script("sum.py", ["-3", "-5"])
        assert result.returncode == 0
        assert int(result.stdout.strip()) == -8

    def test_sum_mixed_signs(self, run_script):
        """Sum of -10 + 3 should be -7."""
        result = run_script("sum.py", ["-10", "3"])
        assert result.returncode == 0
        assert int(result.stdout.strip()) == -7

    def test_sum_large_numbers(self, run_script):
        """Sum of 999999 + 1 should be 1000000."""
        result = run_script("sum.py", ["999999", "1"])
        assert result.returncode == 0
        assert int(result.stdout.strip()) == 1000000

    def test_sum_is_commutative(self, run_script):
        """sum(a, b) should equal sum(b, a)."""
        result1 = run_script("sum.py", ["7", "3"])
        result2 = run_script("sum.py", ["3", "7"])
        assert result1.returncode == 0
        assert result2.returncode == 0
        assert result1.stdout.strip() == result2.stdout.strip()

    def test_missing_args_fails(self, run_script):
        """Running with no arguments should fail."""
        result = run_script("sum.py", [])
        assert result.returncode != 0
