import pytest
from src.pigeon import Pigeon
from src.pigeon_container import PigeonContainer


@pytest.fixture()
def default_pigeon():
    return Pigeon(1, 1)


@pytest.fixture
def container():
    return PigeonContainer()


@pytest.fixture
def _add_default_pigeon(container, default_pigeon):
    container.add(default_pigeon)


@pytest.mark.usefixtures('_add_default_pigeon')
def test_key_not_int(container, default_pigeon):
    with pytest.raises(IndexError):
        container['i'] = default_pigeon


@pytest.mark.usefixtures('_add_default_pigeon')
def test_key_not_exist(container, default_pigeon):
    with pytest.raises(IndexError):
        assert container[1] == default_pigeon


@pytest.mark.usefixtures('_add_default_pigeon')
def test_add_one_pigeon(container, default_pigeon):
    assert container[0] == default_pigeon


@pytest.mark.usefixtures('_add_default_pigeon')
def test_add_multiple_pigeons(container, default_pigeon):
    container.add(Pigeon(2, 2))
    assert container[0] == default_pigeon
    assert container[1] == Pigeon(2, 2)


def test_len_no_pigeons(container):
    assert len(container) == 0


def test_len_one_pigeon(container, default_pigeon):
    container.add(default_pigeon)
    assert len(container) == 1


@pytest.mark.usefixtures('_add_default_pigeon')
def test_len_multiple_pigeons(container):
    container.add(Pigeon(2, 1))
    assert len(container) == 2
