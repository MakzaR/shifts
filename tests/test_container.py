import pytest
from src.pigeon import Pigeon
from src.pigeon_container import PigeonContainer


@pytest.fixture(autouse=True)
def default_pigeon():
    return Pigeon(1, 1)


@pytest.fixture
def container():
    return PigeonContainer()


def test_add_one_pigeon(container, default_pigeon):
    container.add(default_pigeon)
    assert container[0] == default_pigeon


def test_add_multiple_pigeons(container, default_pigeon):
    container.add(default_pigeon)
    container.add(Pigeon(2, 2))
    assert container[0] == default_pigeon
    assert container[1] == Pigeon(2, 2)


def test_len_no_pigeons(container):
    assert len(container) == 0


def test_len_one_pigeon(container, default_pigeon):
    container.add(default_pigeon)
    assert len(container) == 1


def test_len_multiple_pigeons(container, default_pigeon):
    container.add(default_pigeon)
    container.add(default_pigeon)
    assert len(container) == 2


def test_to_str_one_pigeon(container, default_pigeon):
    container.add(default_pigeon)
    assert str(container) == 'pigeons: \n' 'index: 1, velocity: 1 \n'


def test_to_str_multiple_pigeons(container, default_pigeon):
    container.add(default_pigeon)
    container.add(Pigeon(2, 2))
    assert str(container) == 'pigeons: \n' 'index: 1, velocity: 1 \nindex: 2, velocity: 2 \n'


def test_to_str_no_pigeons(container):
    assert str(container) == 'No pigeons added'


def test_sort(container):
    container.add(Pigeon(1, 10))
    container.add(Pigeon(2, 20))
    container.add(Pigeon(3, 6))
    container.add(Pigeon(4, 1))
    assert (
        container.sort() == 'pigeons: \n'
        'index: 4, velocity: 1 \nindex: 3, velocity: 6 \nindex: 1, velocity: 10 \nindex: 2, velocity: 20 \n'
    )
