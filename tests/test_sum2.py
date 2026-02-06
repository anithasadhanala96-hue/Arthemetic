"""
Tests for sum2.py

Based on the file name 'sum2.py' and its loop structure:
This script should print the running cumulative sum of natural numbers from 1 to N.
For N=5, expected output lines: 1, 3, 6, 10, 15
CLI args: one number (the upper bound N)
"""

import pytest


class TestSum2:

    def test_sum2_n_equals_1(self, run_script):
        """For n=1, output should be a single line: 1."""
        result = run_script("sum2.py", ["1"])
        assert result.returncode == 0
        lines = result.stdout.strip().splitlines()
        assert len(lines) == 1
        assert int(lines[0].strip()) == 1

    def test_sum2_n_equals_5(self, run_script):
        """For n=5, running sums should be 1, 3, 6, 10, 15."""
        result = run_script("sum2.py", ["5"])
        assert result.returncode == 0
        lines = result.stdout.strip().splitlines()
        assert len(lines) == 5
        expected = [1, 3, 6, 10, 15]
        for i, line in enumerate(lines):
            assert int(line.strip()) == expected[i]

    def test_sum2_n_equals_3(self, run_script):
        """For n=3, running sums should be 1, 3, 6."""
        result = run_script("sum2.py", ["3"])
        assert result.returncode == 0
        lines = result.stdout.strip().splitlines()
        assert len(lines) == 3
        expected = [1, 3, 6]
        for i, line in enumerate(lines):
            assert int(line.strip()) == expected[i]

    def test_sum2_final_line_is_total(self, run_script):
        """The last line for n=10 should be 55 (sum of 1..10)."""
        result = run_script("sum2.py", ["10"])
        assert result.returncode == 0
        lines = result.stdout.strip().splitlines()
        assert int(lines[-1].strip()) == 55

    def test_sum2_n_equals_0_produces_no_output(self, run_script):
        """For n=0, there should be no output."""
        result = run_script("sum2.py", ["0"])
        assert result.returncode == 0
        output = result.stdout.strip()
        assert output == ""

    def test_sum2_number_of_lines_matches_n(self, run_script):
        """For n=7, there should be exactly 7 lines of output."""
        result = run_script("sum2.py", ["7"])
        assert result.returncode == 0
        lines = result.stdout.strip().splitlines()
        assert len(lines) == 7

    def test_sum2_missing_arg_fails(self, run_script):
        """Running with no argument should fail."""
        result = run_script("sum2.py", [])
        assert result.returncode != 0
