import pytest
from src.pigeon import Pigeon


@pytest.fixture
def default_pigeon():
    return Pigeon(1, 1)


def test_init(default_pigeon):
    assert default_pigeon.index == 1
    assert default_pigeon.velocity == 1


def test_str(default_pigeon):
    assert 'index: 1, velocity: 1' == str(default_pigeon)


def test_lt_true():
    first_pig = Pigeon(1, 1)
    sec_pig = Pigeon(2, 2)
    assert first_pig < sec_pig


def test_lt_false():
    first_pig = Pigeon(2, 2)
    sec_pig = Pigeon(1, 1)
    assert not first_pig < sec_pig


def test_lt_same_pigeon():
    first_pig = Pigeon(1, 1)
    sec_pig = Pigeon(1, 1)
    assert not first_pig < sec_pig


def test_eq():
    first_pig = Pigeon(1, 1)
    sec_pig = Pigeon(1, 1)
    assert first_pig == sec_pig


def test_unequal_same_class():
    first_pig = Pigeon(1, 1)
    sec_pig = Pigeon(2, 2)
    assert not first_pig == sec_pig


def test_unequal_diff_class():
    pigeon = Pigeon(1, 1)
    assert not pigeon == 1
