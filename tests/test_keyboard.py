"""Здесь надо написать тесты с использованием pytest для модуля keyboard."""
import pytest
from src.keyboard import Keyboard

kb = Keyboard('Dark Project KD87A', 9600, 5)


def test_init():
    assert kb.name == "Dark Project KD87A"
    assert kb.price == 9600
    assert kb.quantity == 5
    assert kb.language == "EN"


def test_language():
    """Название товара - EN"""
    assert str(kb.language) != "RU"


def test_change_lang():
    """EN по умолчанию, поэтому при change_lang получаем RU.
    Еще раз change_lang дает нам EN
    """
    kb.change_lang()
    assert str(kb.language) == "RU"
    kb.change_lang()
    assert str(kb.language) == "EN"
