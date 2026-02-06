"""
Tests for reversalnumber.py

Based on the file name 'reversalnumber.py':
This script should reverse the digits of a given number.
CLI args: one number (or numeric string)
"""

import pytest


class TestReversalNumber:

    def test_reverse_123(self, run_script):
        """Reverse of 123 should be 321."""
        result = run_script("reversalnumber.py", ["123"])
        assert result.returncode == 0
        assert result.stdout.strip() == "321"

    def test_reverse_single_digit(self, run_script):
        """Reverse of 5 should be 5."""
        result = run_script("reversalnumber.py", ["5"])
        assert result.returncode == 0
        assert result.stdout.strip() == "5"

    def test_reverse_100(self, run_script):
        """Reverse of 100 should be 001 (string reversal)."""
        result = run_script("reversalnumber.py", ["100"])
        assert result.returncode == 0
        assert result.stdout.strip() == "001"

    def test_reverse_palindrome_stays_same(self, run_script):
        """Reverse of 121 should be 121."""
        result = run_script("reversalnumber.py", ["121"])
        assert result.returncode == 0
        assert result.stdout.strip() == "121"

    def test_reverse_large_number(self, run_script):
        """Reverse of 123456789 should be 987654321."""
        result = run_script("reversalnumber.py", ["123456789"])
        assert result.returncode == 0
        assert result.stdout.strip() == "987654321"

    def test_reverse_two_digits(self, run_script):
        """Reverse of 42 should be 24."""
        result = run_script("reversalnumber.py", ["42"])
        assert result.returncode == 0
        assert result.stdout.strip() == "24"

    def test_reverse_all_same_digits(self, run_script):
        """Reverse of 1111 should be 1111."""
        result = run_script("reversalnumber.py", ["1111"])
        assert result.returncode == 0
        assert result.stdout.strip() == "1111"

    def test_missing_arg_fails(self, run_script):
        """Running with no argument should fail."""
        result = run_script("reversalnumber.py", [])
        assert result.returncode != 0
