def main():
    import sys
    import coverage
    import pytest
    import glob

    cov = coverage.Coverage()
    cov.start()
    print("Beginning testing...")
    errno = pytest.main(glob.glob("./problems/**/test.py"))

    cov.stop()
    cov.save()

    cov.html_report()

    print("Wrote coverage report to htmlcov directory")
    sys.exit(errno)


if __name__ == "__main__":
    main()
