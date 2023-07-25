"""Здесь надо написать тесты с использованием pytest для модуля phone."""
import pytest
from src.phone import Phone


@pytest.fixture
def phone1():
    return Phone("Смартфон", 10000, 20, 2)


def test_phone_init(phone1):
    assert phone1.name == "Смартфон"
    assert phone1.price == 10000
    assert phone1.quantity == 20
    assert phone1.number_of_sim == 2


def test_calculate_total_price(phone1):
    assert phone1.calculate_total_price() == 200000


def test_apply_discount(phone1):
    phone1.apply_discount()
    assert phone1.price == 10000


def test_name_setter(phone1):
    phone1.name = 'Смартфонище'
    assert phone1.name == 'Смартфонищ'



def test_string_to_number():
    assert Phone.string_to_number('5') == 5
    assert Phone.string_to_number('5.0') == 5
    assert Phone.string_to_number('5.5') == 5


phone2 = Phone("Смартфон", 10000, 20, 2)


def test_str():
    assert str(phone2) == 'Смартфон'


def test_repr():
    assert repr(phone2) == "Phone('Смартфон', 10000, 20, 2)"


phone3 = Phone("Смартфон", 10000, 25, 2)


def test_add():
    assert phone3 + phone2 == 45
