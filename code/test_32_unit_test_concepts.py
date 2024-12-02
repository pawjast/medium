# ---
# IMPORTS
# ---
from unittest.mock import patch
import datetime
import pytest


# ---
# FUNCTION DEFINITION
# ---
def power(base: float, exponent: int) -> float:
    """Calculate the power of a number.

    Args:
        base (float): The base number to be raised.
        exponent (int): The exponent to raise the base to.

    Returns:
        float: The result.
    """
    return base ** exponent

# ---
# INDIVIDUAL UNIT TESTS
# ---
def test_power_of_zero():
    assert power(4, 0) == 1

def test_power_of_one():
    assert power(4, 1) == 4

def test_fractional_exponent():
    assert power(4, 0.5) == 2

def test_negative_exponent():
    assert power(4, -1) == 0.25

# ---
# FIXTURE
# ---

@pytest.fixture
def base():
    return 4

# ---
# UNIT TESTS USING FIXTURE
# ---
def test_power_of_zero_1(base):
    assert power(base, 0) == 1

def test_power_of_one_1(base):
    assert power(base, 1) == 4

def test_fractional_exponent_1(base):
    assert power(base, 0.5) == 2

def test_negative_exponent_1(base):
    assert power(base, -1) == 0.25

# ---
# PARAMETRIZED TEST
# ---

@pytest.mark.parametrize(
        "base, exponent, expected_result",
        [
            pytest.param(
                4,  # base value
                0,  # exponent value
                1,  # expected result
                id = "power_of_zero"
            ),
            pytest.param(
                4, 1, 4,
                id = "power_of_one"
            ),
            pytest.param(
                4, 0.5, 2,
                id = "fractional_exponent"
            ),
            pytest.param(
                4, -1, 0.25,
                id = "negative_exponent"
            ),
        ]
)
def test_parametrized(base, exponent, expected_result):
    assert power(base, exponent) == expected_result

# ---
# MOCKING AND PATCHING
# ---

# ---
# FUNCTION DEFINITION
# ---
def is_it_weekend_yet():
    """Check if it's weekend

    Returns:
        (bool, datetime.datetime): outcome of the check
    """ 
    today = datetime.datetime.now()
    if today.weekday() > 4:
        # Yeah, It's weekend baby!
        return True, today
    else:
        # Sorry, it's not weekend yet
        return False, today


def test_if_weekend_no():
    # Tuesday
    # Use the actual `datetime` module to create specific date
    weekday_value = datetime.datetime(year=2024, month=10, day=1)
    with patch("datetime.datetime") as mock_datetime:
        mock_datetime.now.return_value = weekday_value
        assert is_it_weekend_yet() == (False, weekday_value)

def test_if_weekend_yes():
    # Saturday
    # Use the actual `datetime` module to create specific date
    weekday_value = datetime.datetime(year=2024, month=10, day=5)
    with patch("datetime.datetime") as mock_datetime:
        mock_datetime.now.return_value = weekday_value
        assert is_it_weekend_yet() == (True, weekday_value)
