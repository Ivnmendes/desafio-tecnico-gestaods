import subprocess
import sys


def test():
    subprocess.run(
        [
            "uv",
            "run",
            "python",
            "-m",
            "unittest",
            "discover",
            "-s",
            "tests",
            "-t",
            ".",
            "-v",
        ]
    )


def test_cov():
    subprocess.run(
        [
            "uv",
            "run",
            "python",
            "-m",
            "pytest",
            "--cov=src",
            "--cov-report=term-missing",
        ]
    )


def lint():
    subprocess.run(["uv", "run", "pre-commit", "run", "--all-files"])


def format():
    subprocess.run(
        ["uv", "run", "pre-commit", "run", "--all-files", "--hook-stage", "manual"]
    )


if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) > 1 else ""
    if arg == "test":
        test()
    elif arg == "tests_cov":
        test_cov()
    elif arg == "lint":
        lint()
    elif arg == "format":
        format()
    else:
        print("Usage: python tasks.py [test|tests_cov|lint|format]")
