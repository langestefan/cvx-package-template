"""Sample python file for testing functions from the source code."""

import pytest
from src.cvx_package_template.hello_world import (
    Calculator,
    calculate_statistics,
    hello_world,
)


def test_hello() -> None:
    """Run a simple test that can use a mock to override online functionality.

    unit_test_mocks: Fixture located in conftest.py, implicitly imported via
    pytest.
    """
    out = hello_world("0")
    assert out == "Hello, 0!" or "string-0" in out, "Expected output did not match"


def test_hello_world_default() -> None:
    """Test hello_world with default parameters."""
    result = hello_world()
    assert result == "Hello, World!"


def test_hello_world_with_name() -> None:
    """Test hello_world with custom name."""
    result = hello_world("Alice")
    assert result == "Hello, Alice!"


def test_hello_world_with_count() -> None:
    """Test hello_world with multiple counts."""
    result = hello_world("Bob", count=3)
    expected = "Hello, Bob!\nHello, Bob!\nHello, Bob!"
    assert result == expected


def test_hello_world_invalid_count() -> None:
    """Test hello_world with invalid count raises ValueError."""
    with pytest.raises(ValueError, match="count must be a positive integer"):
        hello_world("Alice", count=0)

    with pytest.raises(ValueError, match="count must be a positive integer"):
        hello_world("Alice", count=-1)


def test_hello_world_invalid_name_type() -> None:
    """Test hello_world with invalid name type raises TypeError."""
    with pytest.raises(TypeError, match="name must be a string or None"):
        hello_world(123)  # type: ignore


def test_calculate_statistics_basic() -> None:
    """Test calculate_statistics with basic input."""
    data = [1, 2, 3, 4, 5]
    result = calculate_statistics(data)  # type: ignore[arg-type]

    assert result["mean"] == 3.0
    assert result["median"] == 3.0
    assert result["min"] == 1.0
    assert result["max"] == 5.0
    assert abs(result["std"] - 1.4142135623730951) < 1e-10


def test_calculate_statistics_single_value() -> None:
    """Test calculate_statistics with single value."""
    data = [42]
    result = calculate_statistics(data)  # type: ignore[arg-type]

    assert result["mean"] == 42.0
    assert result["median"] == 42.0
    assert result["min"] == 42.0
    assert result["max"] == 42.0
    assert result["std"] == 0.0


def test_calculate_statistics_mixed_types() -> None:
    """Test calculate_statistics with mixed int and float."""
    data = [1, 2.5, 3, 4.5, 5]
    result = calculate_statistics(data)

    assert result["mean"] == 3.2
    assert result["median"] == 3.0
    assert result["min"] == 1.0
    assert result["max"] == 5.0


def test_calculate_statistics_empty_list() -> None:
    """Test calculate_statistics with empty list raises ValueError."""
    with pytest.raises(ValueError, match="data cannot be empty"):
        calculate_statistics([])


def test_calculate_statistics_invalid_type() -> None:
    """Test calculate_statistics with non-list input raises TypeError."""
    with pytest.raises(TypeError, match="data must be a list"):
        calculate_statistics("not a list")  # type: ignore


def test_calculate_statistics_non_numeric() -> None:
    """Test calculate_statistics with non-numeric values raises ValueError."""
    with pytest.raises(ValueError, match="data must contain only numeric values"):
        calculate_statistics([1, 2, "three", 4])  # type: ignore


class TestCalculator:
    """Test class for Calculator functionality."""

    def test_calculator_init_default(self) -> None:
        """Test Calculator initialization with default value."""
        calc = Calculator()
        assert calc.value == 0.0
        assert calc.get_history() == ["Initialized with 0"]

    def test_calculator_init_with_value(self) -> None:
        """Test Calculator initialization with custom value."""
        calc = Calculator(10)
        assert calc.value == 10.0
        assert calc.get_history() == ["Initialized with 10"]

    def test_calculator_init_invalid_type(self) -> None:
        """Test Calculator initialization with invalid type raises TypeError."""
        with pytest.raises(TypeError, match="initial_value must be a number"):
            Calculator("not a number")  # type: ignore[arg-type]

    def test_calculator_add(self) -> None:
        """Test Calculator add method."""
        calc = Calculator(10)
        result = calc.add(5)
        assert result == 15.0
        assert calc.value == 15.0
        assert "Added 5" in calc.get_history()

    def test_calculator_add_invalid_type(self) -> None:
        """Test Calculator add with invalid type raises TypeError."""
        calc = Calculator()
        with pytest.raises(TypeError, match="x must be a number"):
            calc.add("not a number")  # type: ignore[arg-type]

    def test_calculator_multiply(self) -> None:
        """Test Calculator multiply method."""
        calc = Calculator(10)
        result = calc.multiply(3)
        assert result == 30.0
        assert calc.value == 30.0
        assert "Multiplied by 3" in calc.get_history()

    def test_calculator_multiply_invalid_type(self) -> None:
        """Test Calculator multiply with invalid type raises TypeError."""
        calc = Calculator()
        with pytest.raises(TypeError, match="x must be a number"):
            calc.multiply("not a number")  # type: ignore[arg-type]

    def test_calculator_reset_default(self) -> None:
        """Test Calculator reset with default value."""
        calc = Calculator(10)
        calc.add(5)
        result = calc.reset()
        assert result == 0.0
        assert calc.value == 0.0
        assert "Reset to 0" in calc.get_history()

    def test_calculator_reset_with_value(self) -> None:
        """Test Calculator reset with custom value."""
        calc = Calculator(10)
        result = calc.reset(20)
        assert result == 20.0
        assert calc.value == 20.0
        assert "Reset to 20" in calc.get_history()

    def test_calculator_reset_invalid_type(self) -> None:
        """Test Calculator reset with invalid type raises TypeError."""
        calc = Calculator()
        with pytest.raises(TypeError, match="new_value must be a number"):
            calc.reset("not a number")  # type: ignore[arg-type]

    def test_calculator_greet_default(self) -> None:
        """Test Calculator greet with default name."""
        calc = Calculator(42)
        result = calc.greet()
        assert result == "Hello Calculator! My current value is 42.0"

    def test_calculator_greet_custom_name(self) -> None:
        """Test Calculator greet with custom name."""
        calc = Calculator(42)
        result = calc.greet("Alice")
        assert result == "Hello Alice! My current value is 42.0"

    def test_calculator_get_history_copy(self) -> None:
        """Test that get_history returns a copy, not the original."""
        calc = Calculator(5)
        calc.add(3)
        history = calc.get_history()
        history.append("Modified outside")

        # Original history should be unchanged
        original_history = calc.get_history()
        assert "Modified outside" not in original_history
        assert len(original_history) == 2

    def test_calculator_complex_operations(self) -> None:
        """Test a sequence of calculator operations."""
        calc = Calculator(10)
        calc.add(5)  # 15
        calc.multiply(2)  # 30
        calc.reset(100)  # 100
        calc.add(-10)  # 90

        assert calc.value == 90.0
        history = calc.get_history()
        assert len(history) == 5
        assert "Initialized with 10" in history
        assert "Added 5" in history
        assert "Multiplied by 2" in history
        assert "Reset to 100" in history
        assert "Added -10" in history
