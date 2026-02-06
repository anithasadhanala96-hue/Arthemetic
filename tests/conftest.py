import subprocess
import sys
import os
import pytest

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


@pytest.fixture
def run_script():
    """Fixture that returns a helper to run a Python script via subprocess."""
    def _run(script_name, args=None, timeout=10):
        script_path = os.path.join(PROJECT_ROOT, script_name)
        cmd = [sys.executable, script_path]
        if args:
            cmd.extend([str(a) for a in args])
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout,
        )
        return result
    return _run


_test_results = []


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Collect the outcome of every test call phase."""
    outcome = yield
    report = outcome.get_result()
    if report.when == "call":
        _test_results.append(report)


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    """Print a clear pass/fail summary at the end of the test run."""
    passed = [r for r in _test_results if r.passed]
    failed = [r for r in _test_results if r.failed]

    terminalreporter.section("Test Run Report")

    terminalreporter.write_line(f"Total tests run : {len(_test_results)}")
    terminalreporter.write_line(f"Passed          : {len(passed)}")
    terminalreporter.write_line(f"Failed          : {len(failed)}")
    terminalreporter.write_line("")

    if failed:
        terminalreporter.write_line("===== FAILED TEST CASES =====", red=True, bold=True)
        for i, report in enumerate(failed, 1):
            terminalreporter.write_line(f"  {i}. {report.nodeid}", red=True)
        terminalreporter.write_line("")

    if passed:
        terminalreporter.write_line("===== PASSED TEST CASES =====", green=True, bold=True)
        for i, report in enumerate(passed, 1):
            terminalreporter.write_line(f"  {i}. {report.nodeid}", green=True)
        terminalreporter.write_line("")
