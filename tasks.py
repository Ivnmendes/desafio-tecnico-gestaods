import subprocess
import sys


def test():
    subprocess.run(["uv", "run", "pytest", "-v", "tests"])


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


def make_migrations():
    subprocess.run(["uv", "run", "python", "src/manage.py", "makemigrations"])


def migrate():
    subprocess.run(["uv", "run", "python", "src/manage.py", "migrate"])


def runserver():
    subprocess.run(["uv", "run", "python", "src/manage.py", "runserver"])


def createsuperuser():
    subprocess.run(["uv", "run", "python", "src/manage.py", "createsuperuser"])


def collectstatic():
    subprocess.run(
        ["uv", "run", "python", "src/manage.py", "collectstatic", "--noinput"]
    )


def shell():
    subprocess.run(["uv", "run", "python", "src/manage.py", "shell"])


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
    elif arg == "mkmig":
        make_migrations()
    elif arg == "mig":
        migrate()
    elif arg == "run":
        runserver()
    elif arg == "csu":
        createsuperuser()
    elif arg == "cs":
        collectstatic()
    elif arg == "shell":
        shell()
    else:
        print(
            "Usage: python tasks.py "
            "["
            "test|"
            "tests_cov|"
            "lint|"
            "format|"
            "makemigrations|"
            "migrate|"
            "runserver|"
            "createsuperuser|"
            "collectstatic|"
            "shell]"
        )
