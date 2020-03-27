import pytest
from src.pigeon import Pigeon


@pytest.fixture
def default_pigeon():
    return Pigeon(1, 1)


def test_init(default_pigeon):
    assert 1 == default_pigeon.index
    assert default_pigeon.velocity == 1


def test_str(default_pigeon):
    assert 'index: 1, velocity: 1' == str(default_pigeon)


def test_lt():
    first_pig = Pigeon(1, 1)
    sec_pig = Pigeon(2, 2)
    assert first_pig < sec_pig


def test_eq():
    first_pig = Pigeon(1, 1)
    sec_pig = Pigeon(1, 1)
    assert first_pig == sec_pig


def test_unequal():
    first_pig = Pigeon(1, 1)
    sec_pig = Pigeon(2, 2)
    assert first_pig != sec_pig
