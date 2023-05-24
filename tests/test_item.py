"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item, InstantiateCSVError
from src.phone import Phone


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


def test_add_():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Наушники", 5000, 8)

    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    phone2 = Phone("Samsung Galaxy", 15_000, 10, 6)

    assert item1 + phone1 == 25
    assert item1 + item2 == 28
    assert phone1 + phone2 == 15


def test_instantiate_no_csv():
    # проверка на отсутствие файла
    try:
        Item.instantiate_from_csv()
    except FileNotFoundError:
        pytest.fail('Файл не найден.')
