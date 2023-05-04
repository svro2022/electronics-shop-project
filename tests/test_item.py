"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item

@pytest.fixture
def test_item():
    return Item("headphones", 2300, 5)

def test_calculate_total_price(test_item):
    assert test_item.calculate_total_price() == 11500

def test_apply_discount(test_item):
    Item.pay_rate = 0.5
    test_item.apply_discount()
    assert test_item.price == 1150

def test_name_getter(test_item):
    assert test_item.name == "headphones"
