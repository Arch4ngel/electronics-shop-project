"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item
from src.item import InstantiateCSVError


@pytest.fixture
def item1():
    return Item("Смартфон", 10000, 20)


def test_item_init(item1):
    assert item1.name == "Смартфон"
    assert item1.price == 10000
    assert item1.quantity == 20


def test_calculate_total_price(item1):
    assert item1.calculate_total_price() == 200000


def test_apply_discount(item1):
    item1.apply_discount()
    assert item1.price == 10000


def test_name_setter(item1):
    item1.name = 'Смартфонище'
    assert item1.name == 'Смартфонищ'


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


item2 = Item("Смартфон", 10000, 20)


def test_str():
    assert str(item2) == 'Смартфон'


def test_repr():
    assert repr(item2) == "Item('Смартфон', 10000, 20)"


item3 = Item("Смартфон", 10000, 25)


def test_add():
    assert item3 + item2 == 45


def test_instantiate_csv_error():
    error = InstantiateCSVError()
    assert str(error) == '_Файл item.csv поврежден_'
