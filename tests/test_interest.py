"""
Tests for Interest.py

Based on the name 'interestfunction' and file name 'Interest.py':
This script should compute Simple Interest = (P * T * R) / 100.
CLI args: principal, time, rate
"""

import pytest


class TestInterest:

    def test_basic_interest_calculation(self, run_script):
        """SI for P=1000, T=2, R=5 should be 100.0."""
        result = run_script("Interest.py", ["1000", "2", "5"])
        assert result.returncode == 0
        tokens = result.stdout.strip().split()
        interest_value = float(tokens[-1])
        assert interest_value == pytest.approx(100.0)

    def test_interest_with_zero_principal(self, run_script):
        """SI for P=0 should be 0 regardless of time and rate."""
        result = run_script("Interest.py", ["0", "5", "10"])
        assert result.returncode == 0
        tokens = result.stdout.strip().split()
        interest_value = float(tokens[-1])
        assert interest_value == pytest.approx(0.0)

    def test_interest_with_zero_rate(self, run_script):
        """SI with R=0 should be 0."""
        result = run_script("Interest.py", ["1000", "5", "0"])
        assert result.returncode == 0
        tokens = result.stdout.strip().split()
        interest_value = float(tokens[-1])
        assert interest_value == pytest.approx(0.0)

    def test_interest_with_zero_time(self, run_script):
        """SI with T=0 should be 0."""
        result = run_script("Interest.py", ["1000", "0", "10"])
        assert result.returncode == 0
        tokens = result.stdout.strip().split()
        interest_value = float(tokens[-1])
        assert interest_value == pytest.approx(0.0)

    def test_interest_all_ones(self, run_script):
        """SI for P=1, T=1, R=1 should be 0.01."""
        result = run_script("Interest.py", ["1", "1", "1"])
        assert result.returncode == 0
        tokens = result.stdout.strip().split()
        interest_value = float(tokens[-1])
        assert interest_value == pytest.approx(0.01)

    def test_interest_large_values(self, run_script):
        """SI for P=100000, T=10, R=8 should be 80000.0."""
        result = run_script("Interest.py", ["100000", "10", "8"])
        assert result.returncode == 0
        tokens = result.stdout.strip().split()
        interest_value = float(tokens[-1])
        assert interest_value == pytest.approx(80000.0)

    def test_interest_missing_args_fails(self, run_script):
        """Running with no arguments should fail."""
        result = run_script("Interest.py", [])
        assert result.returncode != 0

    def test_interest_output_contains_principal_label(self, run_script):
        """Output should contain the word 'principal' as a label."""
        result = run_script("Interest.py", ["1000", "2", "5"])
        assert result.returncode == 0
        assert "principal" in result.stdout.lower()
