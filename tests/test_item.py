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


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5
    assert Item.string_to_number('0') == 0
    assert Item.string_to_number('6.66') == 6


def test_namesetter_true_name(test_item):
    test_item.name = "SmartPhone"
    assert test_item.name == "SmartPhone"


def test_namesetter_false_name(test_item):
    with pytest.raises(ValueError):
        test_item.name = "SuperSmartPhone"


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5


def test_repr():
    item = Item("Смартфон", 10000, 20)
    expected = "Item('Смартфон', 10000, 20)"
    assert repr(item) == expected


def test_str():
    item = Item("Смартфон", 10000, 20)
    expected = "Смартфон"
    assert str(item) == expected
