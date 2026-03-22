from ex_pipeline import add


def test_add_positive_numbers() -> None:
    assert add(1, 2) == 3


def test_add_negative_numbers() -> None:
    assert add(-1, -2) == -3


def test_add_zero() -> None:
    assert add(0, 0) == 0


def test_add_mixed() -> None:
    assert add(-1, 1) == 0
