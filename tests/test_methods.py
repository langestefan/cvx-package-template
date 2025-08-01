"""Sample python file for testing functions from the source code."""

from package.hello_world import hello_world


def hello_test() -> None:
    """Demonstrate the expected usage for various test cases.

    Pytest will not execute this code directly, since the function does not
    contain the suffix "test".
    """
    hello_world()


def test_hello(unit_test_mocks: None) -> None:  # noqa: ARG001
    """Run a simple test that can use a mock to override online functionality.

    unit_test_mocks: Fixture located in conftest.py, implicitly imported via
    pytest.
    """
    hello_test()


def test_int_hello() -> None:
    """Mark as an integration test if the name contains "_init_".

    See:
    https://docs.pytest.org/en/6.2.x/example/markers.html#
    automatically-adding-markers-based-on-test-names
    """
    hello_test()
