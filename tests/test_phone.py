"""Здесь надо написать тесты с использованием pytest для модуля phone."""
import pytest
from src.phone import Phone


@pytest.fixture
def test_phone():
    return Phone("iPhone 14", 120000, 5, 2)


def test_repr(test_phone):
    assert test_phone.__repr__() == "Phone('iPhone 14', 120000, 5, 2)"


def test_number_of_sim_getter(test_phone):
    assert test_phone.number_of_sim == 2


def test_number_of_sim_setter(test_phone):
    assert test_phone.number_of_sim == 2
    with pytest.raises(ValueError):
        test_phone.number_of_sim = 0
