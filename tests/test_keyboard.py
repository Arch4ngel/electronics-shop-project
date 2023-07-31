import pytest
from src.keyboard import Keyboard


kb = Keyboard('Dark Project KD87A', 9600, 5)


def test_keyboard():
    assert str(kb) == "Dark Project KD87A"
    assert str(kb.language) == "EN"
    with pytest.raises(AttributeError):
        kb.language = 'CH'


def test_change_lang():
    kb.change_lang()
    assert str(kb.language) == "RU"
    kb.change_lang()
    assert str(kb.language) == "EN"
