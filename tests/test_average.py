"""
Tests for average.py

Based on the name 'averagefunction' and file name 'average.py':
This script should compute the arithmetic average of 3 numbers provided as CLI args.
Expected formula: (arg1 + arg2 + arg3) / 3
"""

import pytest


class TestAverage:

    def test_average_of_equal_numbers(self, run_script):
        """Average of three identical numbers should be that number."""
        result = run_script("average.py", ["10", "10", "10"])
        assert result.returncode == 0
        assert float(result.stdout.strip()) == pytest.approx(10.0)

    def test_average_of_different_positive_numbers(self, run_script):
        """Average of 10, 20, 30 should be 20.0."""
        result = run_script("average.py", ["10", "20", "30"])
        assert result.returncode == 0
        assert float(result.stdout.strip()) == pytest.approx(20.0)

    def test_average_with_zero(self, run_script):
        """Average of 0, 0, 0 should be 0.0."""
        result = run_script("average.py", ["0", "0", "0"])
        assert result.returncode == 0
        assert float(result.stdout.strip()) == pytest.approx(0.0)

    def test_average_of_negative_numbers(self, run_script):
        """Average of -10, -20, -30 should be -20.0."""
        result = run_script("average.py", ["-10", "-20", "-30"])
        assert result.returncode == 0
        assert float(result.stdout.strip()) == pytest.approx(-20.0)

    def test_average_of_mixed_sign_numbers(self, run_script):
        """Average of -10, 0, 10 should be 0.0."""
        result = run_script("average.py", ["-10", "0", "10"])
        assert result.returncode == 0
        assert float(result.stdout.strip()) == pytest.approx(0.0)

    def test_average_produces_decimal_result(self, run_script):
        """Average of 1, 2, 3 should be 2.0."""
        result = run_script("average.py", ["1", "2", "3"])
        assert result.returncode == 0
        assert float(result.stdout.strip()) == pytest.approx(2.0)

    def test_average_non_integer_result(self, run_script):
        """Average of 1, 2, 4 should be 2.333..."""
        result = run_script("average.py", ["1", "2", "4"])
        assert result.returncode == 0
        assert float(result.stdout.strip()) == pytest.approx(2.3333333333, rel=1e-5)

    def test_average_missing_args_fails(self, run_script):
        """Running with no arguments should exit with non-zero."""
        result = run_script("average.py", [])
        assert result.returncode != 0

    def test_average_large_numbers(self, run_script):
        """Average of large numbers: (1000000+2000000+3000000)/3 = 2000000."""
        result = run_script("average.py", ["1000000", "2000000", "3000000"])
        assert result.returncode == 0
        assert float(result.stdout.strip()) == pytest.approx(2000000.0)
