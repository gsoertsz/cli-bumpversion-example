import os


def pytest_runtest_setup():
    """
    Set environment variables needed for tests

    pytest_runtest_setup() is a hook that is called for tests
    that are in the same directory as the `conftest.py` file
    it is in.

    ref: https://docs.pytest.org/en/latest/writing_plugins.html#conftest-py-local-per-directory-plugins
    """
    pass
