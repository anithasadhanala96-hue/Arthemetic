"""
Tests for palindromenumber.py

Based on the file name 'palindromenumber.py':
This script should check whether a given number is a palindrome.
A palindrome number reads the same forwards and backwards (e.g., 121, 1331, 5).
CLI args: one number

NOTE: The current implementation has a SyntaxError ('break' outside loop).
These tests define the EXPECTED behavior based on the file name.
They will fail until the bug is fixed.
"""

import pytest


class TestPalindromeNumber:

    def test_palindrome_single_digit(self, run_script):
        """Single digit numbers are always palindromes."""
        result = run_script("palindromenumber.py", ["5"])
        assert result.returncode == 0
        assert "palindrome" in result.stdout.lower()

    def test_palindrome_121(self, run_script):
        """121 is a palindrome."""
        result = run_script("palindromenumber.py", ["121"])
        assert result.returncode == 0
        assert "palindrome" in result.stdout.lower()

    def test_palindrome_1331(self, run_script):
        """1331 is a palindrome."""
        result = run_script("palindromenumber.py", ["1331"])
        assert result.returncode == 0
        assert "palindrome" in result.stdout.lower()

    def test_not_palindrome_123(self, run_script):
        """123 is NOT a palindrome."""
        result = run_script("palindromenumber.py", ["123"])
        assert result.returncode == 0
        output = result.stdout.lower()
        is_positive_claim = "is a palindrome" in output and "not" not in output
        assert not is_positive_claim

    def test_not_palindrome_100(self, run_script):
        """100 is NOT a palindrome (reversed is 001)."""
        result = run_script("palindromenumber.py", ["100"])
        assert result.returncode == 0
        output = result.stdout.lower()
        is_positive_claim = "is a palindrome" in output and "not" not in output
        assert not is_positive_claim

    def test_palindrome_0(self, run_script):
        """0 is a palindrome (single digit)."""
        result = run_script("palindromenumber.py", ["0"])
        assert result.returncode == 0
        assert "palindrome" in result.stdout.lower()

    def test_palindrome_large_number(self, run_script):
        """12321 is a palindrome."""
        result = run_script("palindromenumber.py", ["12321"])
        assert result.returncode == 0
        assert "palindrome" in result.stdout.lower()

    def test_script_runs_without_error(self, run_script):
        """The script should run without SyntaxError or runtime exceptions."""
        result = run_script("palindromenumber.py", ["121"])
        assert result.returncode == 0
        assert "SyntaxError" not in result.stderr
        assert "Error" not in result.stderr

    def test_missing_arg_fails(self, run_script):
        """Running with no argument should fail."""
        result = run_script("palindromenumber.py", [])
        assert result.returncode != 0
