import pytest
from src.pigeon import Pigeon


@pytest.fixture
def default_pigeon():
    return Pigeon(1, 1)


def test_init(default_pigeon):
    assert default_pigeon.index == 1
    assert default_pigeon.velocity == 1


def test_lt_true(default_pigeon):
    sec_pig = Pigeon(2, 2)
    assert default_pigeon < sec_pig


def test_lt_false(default_pigeon):
    first_pig = Pigeon(2, 2)
    assert not first_pig < default_pigeon


def test_lt_same_pigeon(default_pigeon):
    assert not default_pigeon < default_pigeon


def test_eq(default_pigeon):
    assert default_pigeon == default_pigeon


def test_unequal_same_class(default_pigeon):
    sec_pig = Pigeon(2, 2)
    assert not default_pigeon == sec_pig


def test_unequal_diff_class(default_pigeon):
    assert not default_pigeon == 1
