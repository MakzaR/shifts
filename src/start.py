import argparse
import sys
from collections import namedtuple
from typing import List

from src.pigeon import Pigeon
from src.pigeon_container import PigeonContainer


def get_permutations(container: PigeonContainer, distance: int) -> int:
    size = len(container)
    perms = 0

    for i in range(size):
        for j in range(size - i - 1):
            if (container[j + 1].velocity * distance) + 1 < container[
                j
            ].velocity * distance:
                temp = container[j]
                container[j] = container[j + 1]
                container[j + 1] = temp
                perms += 1
    return perms


def start(number: int, distance: int, velocities: List) -> int:
    container = PigeonContainer()
    for i in range(number):
        container.add(Pigeon(i, velocities[i]))

    return get_permutations(container, distance)


def check_args(number, distance, velocities) -> bool:
    return (
        number is not None
        and distance is not None
        and (velocities is not None and len(velocities) == number)
    )


def parse_arguments(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', dest='number', type=int)
    parser.add_argument('-s', dest='distance', type=int)
    parser.add_argument('-v', dest='velocities', type=int, nargs='*')

    return parser.parse_args(args)


def get_args():
    parser = parse_arguments(sys.argv[1:])
    Args = namedtuple('Args', ['number', 'distance', 'velocities'])
    args = Args(parser.number, parser.distances, parser.velocities)

    return args


def get_result(args):
    if check_args(args.number, args.distance, args.velocities):
        return start(args.number, args.distance, args.velocities)
    return 'use --help'


def main():
    print(get_result(get_args()))
