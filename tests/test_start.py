import pytest
from src.pigeon import Pigeon
from src.pigeon_container import PigeonContainer
from src.start import check_args, get_permutations, get_result, parse_arguments, start


@pytest.fixture
def container():
    return PigeonContainer()


def test_check_right_args():
    assert check_args(3, 10, [1, 1, 1])


def test_check_wrong_args():
    assert not check_args(2, 10, [1, 1, 1])


def test_printing_with_right_args():
    args = [3, 10, [1, 1, 1]]
    assert get_result(args) == 0


def test_printing_with_wrong_args():
    args = [3, 10, [1, 1, 1, 1]]
    assert get_result(args) == 'use --help'


def test_perms_no_permutations(container):
    container.add(Pigeon(1, 10))
    container.add(Pigeon(2, 10))
    assert get_permutations(container, 10) == 0


def test_perms_one_permutation(container):
    container.add(Pigeon(1, 10))
    container.add(Pigeon(2, 9))
    assert get_permutations(container, 10) == 1


def test_perms_multiple_permutations(container):
    container.add(Pigeon(1, 10))
    container.add(Pigeon(2, 9))
    container.add(Pigeon(3, 8))
    assert get_permutations(container, 10) == 3


def test_start():
    assert start(3, 10, [10, 9, 8]) == 3


def test_parsing():
    args = parse_arguments(['-n', '3', '-s', '10', '-v', '10', '10', '10'])
    assert args.number == 3
    assert args.distance == 10
    assert args.velocities == [10, 10, 10]
