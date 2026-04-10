# ---
# IMPORTS
# ---
import pytest
import sys
from pathlib import Path
import time


# ---
# ANATOMY OF TEST
# ---
def say_hi():
    return "Hi"


def test_say_hi():
    output = say_hi()
    assert output == "Hello"

# ---
# SKIPPING SINGLE FUNCTION
# ---


# Function
def add_2(x):
    return x * 2


# Test
@pytest.mark.skip()
def test_add_2():
    """Just skip test, no explanation"""
    ...


# Functions
def multiply_by_2(x):
    return x + 2


def equals_2(x):
    ...


# Tests
@pytest.mark.skip(reason="WIP - test not implemented")
def test_multiply_by_2():
    """Skip, test wasn't implemented"""
    ...


@pytest.mark.skip(reason="WIP - function not implemented")
def test_equals_2():
    """Skip, we've got a test case, but no function yet."""
    assert equals_2(2)


# ---
# SKIPPING METHODS OF CLASSES
# ---
def simple_calc(x, y, action):
    match action:
        case "add":
            return x + y
        case "multiply":
            return x * y


class TestSimpleCalc:
    def test_adding(self):
        output = simple_calc(1, 1, "add")
        assert output == 2

    def test_multiplying(self):
        output = simple_calc(2, 3, "multiply")
        assert output == 6

    @pytest.mark.skip(reason="WIP, function not implemented")
    def test_subtracting(self):
        output = simple_calc(2, 1, "subtract")
        assert output == 1


# ---
# SKIPPING WHOLE CLASSES
# ---
def duplicate(item):
    return f"{item} {item}"


@pytest.mark.skip(reason="deprecated code")
class TestDuplicate:
    def test_duplicating_string(self):
        output = duplicate("a")
        assert output == "a a"

    def test_duplicating_number(self):
        output = duplicate(1)
        assert output == "1 1"


# ---
# SKIPPING A CASE IN PARAMETRIZED TEST
# ---
def count_to(number):
    return list(range(1, number+1))


@pytest.mark.parametrize(
    ("number", "expected"),
    [
        pytest.param(
            3,
            [1, 2, 3],
            id="count to 3",
        ),
        pytest.param(
            5,
            [1, 2, 3, 4, 5],
            id="count to 5",
        ),
        pytest.param(
            4.5,
            [1, 2, 3, 4],
            id="count to 4",
            marks=pytest.mark.skip(reason="handling floats not implemented yet"),
        ),
    ]
)
def test_count_to(number, expected):
    output = count_to(number)
    assert output == expected


# ---
# SKIPPING ALL PARAMETRIZED TESTS
# ---
@pytest.mark.parametrize(
    ("number", "expected"),
    [
        pytest.param(
            3,
            [1, 2, 3],
            id="count to 3",
        ),
        pytest.param(
            5,
            [1, 2, 3, 4, 5],
            id="count to 5",
        ),
    ]
)
@pytest.mark.skip(reason="Skip all - why not?!")
def test_count_to_again(number, expected):
    output = count_to(number)
    assert output == expected

# ---
# DYNAMIC SKIPPING
# ---
def test_folder():
    if not Path("some_folder").is_dir():
        pytest.skip(reason="Folder doesn't exists!")

    # Actual test implementation goes here


# ---
# SKIPPING FAILED TEST
# ---

def taller_than_jordan(height):
    return height > 1.98


@pytest.mark.xfail(reason="BUG: function doesn't handle string inputs yet")
def test_taller_than_jordan_1():
    taller_than_jordan("2.0")


@pytest.mark.xfail(reason="Is this a bug?")
def test_taller_than_jordan_2():
    taller_than_jordan(2.0)


@pytest.mark.xfail(reason="Let me know if it doesn't fail!", strict=True)
def test_taller_than_jordan_3():
    taller_than_jordan(1 + 1)


# ---
# CONDITIONAL SKIP
# ---
@pytest.mark.skipif(sys.platform != "win", reason="Windows test")
def test_exe():
    assert True


# ---
# MARK TEST
# ---
@pytest.mark.very_slow
def test_something_super_slow():
    time.sleep(3)
    assert True
