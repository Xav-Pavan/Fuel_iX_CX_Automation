import pytest
import allure


# Function to be tested
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


# Pytest fixture
@pytest.fixture
def sample_numbers():
    with allure.step("Setting up test data"):
        num1, num2 = 10, 5
        yield num1, num2


# Test case using fixture
@allure.feature("Addition Functionality")
def test_add(sample_numbers):
    with allure.step("Extract test numbers"):
        num1, num2 = sample_numbers

    with allure.step("Perform addition operation"):
        result = add(num1, num2)

    with allure.step("Verify the addition result"):
        assert result == 15, "Addition test failed!"


@allure.feature("Subtraction Functionality")
def test_subtract(sample_numbers):
    with allure.step("Extract test numbers"):
        num1, num2 = sample_numbers

    with allure.step("Perform subtraction operation"):
        result = subtract(num1, num2)

    with allure.step("Verify the subtraction result"):
        assert result == 5, "Subtraction test failed!"


# Parameterized test case with Allure reporting
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0)
])
@allure.feature("Parameterized Addition Test")
def test_add_param(a, b, expected):
    with allure.step(f"Adding {a} + {b}"):
        result = add(a, b)

    with allure.step(f"Verify the result is {expected}"):
        assert result == expected, f"Addition failed for inputs: {a}, {b}"
