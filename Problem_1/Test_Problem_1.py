from Problem_1 import gauss_formula, sum_multiples_3_and_5
import pytest

@pytest.mark.parametrize("test_input, expected", [(10, 23), (100, 2318)])
def test_sum_multiples(test_input, expected):
    assert sum_multiples_3_and_5(test_input) == expected

@pytest.mark.parametrize("test_input, expected", [(5, 15), (10, 55)])
def test_gauss_formula(test_input, expected):
    assert gauss_formula(test_input) == expected
