import pytest

from ex_pipeline import add, divide


def test_add_positive_numbers() -> None:
    assert add(1, 2) == 3


def test_add_negative_numbers() -> None:
    assert add(-1, -2) == -3


def test_add_zero() -> None:
    assert add(0, 0) == 0


def test_add_mixed() -> None:
    assert add(-1, 1) == 0


def test_divide_basic() -> None:
    assert divide(10, 2) == 5.0


def test_divide_negative() -> None:
    assert divide(-10, 2) == -5.0


def test_divide_returns_float() -> None:
    assert divide(7, 2) == 3.5


def test_divide_by_zero_raises_zero_division_error() -> None:
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        divide(1, 0)
