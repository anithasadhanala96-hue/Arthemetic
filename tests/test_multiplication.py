"""
Tests for multiplication.py

Based on the file name 'multiplication.py':
This script should print a multiplication table.
CLI args: tableendnumber (rows), tablenumber (the number whose table to print)
Expected output format per line: "<tablenumber> x <count> = <product>"
"""

import pytest


class TestMultiplication:

    def test_table_of_5_up_to_3(self, run_script):
        """Table of 5, 3 rows: 5x1=5, 5x2=10, 5x3=15."""
        result = run_script("multiplication.py", ["3", "5"])
        assert result.returncode == 0
        lines = result.stdout.strip().splitlines()
        assert len(lines) == 3
        assert "5" in lines[0] and "1" in lines[0]
        assert "10" in lines[1]
        assert "15" in lines[2]

    def test_table_of_2_up_to_5(self, run_script):
        """Table of 2, 5 rows should produce 5 lines."""
        result = run_script("multiplication.py", ["5", "2"])
        assert result.returncode == 0
        lines = result.stdout.strip().splitlines()
        assert len(lines) == 5

    def test_table_of_2_up_to_5_values(self, run_script):
        """Verify actual multiplication values for table of 2."""
        result = run_script("multiplication.py", ["5", "2"])
        assert result.returncode == 0
        lines = result.stdout.strip().splitlines()
        expected_products = [2, 4, 6, 8, 10]
        for i, line in enumerate(lines):
            assert str(expected_products[i]) in line

    def test_table_of_1(self, run_script):
        """Table of 1 up to 5: products should be 1,2,3,4,5."""
        result = run_script("multiplication.py", ["5", "1"])
        assert result.returncode == 0
        lines = result.stdout.strip().splitlines()
        assert len(lines) == 5
        for i, line in enumerate(lines, 1):
            assert str(i) in line

    def test_single_row_table(self, run_script):
        """Table with end=1 should produce exactly 1 line."""
        result = run_script("multiplication.py", ["1", "7"])
        assert result.returncode == 0
        lines = result.stdout.strip().splitlines()
        assert len(lines) == 1
        assert "7" in lines[0]

    def test_table_of_10_up_to_10(self, run_script):
        """Table of 10, 10 rows. Last line should contain 100."""
        result = run_script("multiplication.py", ["10", "10"])
        assert result.returncode == 0
        lines = result.stdout.strip().splitlines()
        assert len(lines) == 10
        assert "100" in lines[-1]

    def test_output_format_contains_x_and_equals(self, run_script):
        """Each output line should contain 'x' and '=' for the format."""
        result = run_script("multiplication.py", ["3", "4"])
        assert result.returncode == 0
        lines = result.stdout.strip().splitlines()
        for line in lines:
            assert "x" in line
            assert "=" in line

    def test_zero_rows_produces_no_output(self, run_script):
        """Table with end=0 should produce no output."""
        result = run_script("multiplication.py", ["0", "5"])
        assert result.returncode == 0
        output = result.stdout.strip()
        assert output == ""

    def test_missing_args_fails(self, run_script):
        """Running with no arguments should fail."""
        result = run_script("multiplication.py", [])
        assert result.returncode != 0
