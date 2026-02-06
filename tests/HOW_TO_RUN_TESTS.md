# How to Run Tests for Arthemetic Project

## Prerequisites

- Python 3.8+
- pytest installed: `pip install pytest`

## Running All Tests

From the project root directory (`Arthemetic/`):

```bash
pytest
```

This will:
1. Discover all test files in the `tests/` directory
2. Run every test case
3. Print verbose PASS/FAIL status for each test
4. Print a **custom report at the end** listing all passed and failed tests

## Running Tests for a Specific File

```bash
# Test only average.py
pytest tests/test_average.py

# Test only Interest.py
pytest tests/test_interest.py

# Test only multiplication.py
pytest tests/test_multiplication.py

# Test only naturalnosum.py
pytest tests/test_naturalnosum.py

# Test only palindromenumber.py
pytest tests/test_palindromenumber.py

# Test only reversalnumber.py
pytest tests/test_reversalnumber.py

# Test only sum.py
pytest tests/test_sum.py

# Test only sum2.py
pytest tests/test_sum2.py
```

## Running a Specific Test Case

```bash
pytest tests/test_sum.py::TestSum::test_sum_positive_numbers
pytest tests/test_average.py::TestAverage::test_average_of_equal_numbers
```

## Understanding the Output

Each test shows:
- **PASSED** (green) — The script behaved as expected
- **FAILED** (red) — The script did NOT behave as expected

At the very end of the run, a **Test Run Report** section appears:

```
===== Test Run Report =====
Total tests run : 65
Passed          : 56
Failed          : 9

===== FAILED TEST CASES =====
  1. tests/test_palindromenumber.py::TestPalindromeNumber::test_palindrome_single_digit
  2. tests/test_palindromenumber.py::TestPalindromeNumber::test_palindrome_121
  ...

===== PASSED TEST CASES =====
  1. tests/test_average.py::TestAverage::test_average_of_equal_numbers
  ...
```

## Test Design Philosophy

These tests are written based on **expected behavior derived from function and file names**, not from the current implementation. If a test fails, it means the source code does not behave as its name implies it should.

For example:
- `palindromenumber.py` has a known SyntaxError (`break` outside loop). All palindrome tests will fail until this bug is fixed.
- Tests define the **specification**, not a mirror of the implementation.

## Project Structure

```
Arthemetic/
  average.py
  Interest.py
  multiplication.py
  naturalnosum.py
  palindromenumber.py
  reversalnumber.py
  sum.py
  sum2.py
  pytest.ini                  # pytest configuration
  tests/
    __init__.py
    conftest.py               # shared fixtures + custom report hook
    test_average.py
    test_interest.py
    test_multiplication.py
    test_naturalnosum.py
    test_palindromenumber.py
    test_reversalnumber.py
    test_sum.py
    test_sum2.py
    HOW_TO_RUN_TESTS.md       # this file
```
