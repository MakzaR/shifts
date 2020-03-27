from __future__ import annotations

from typing import List

from src.pigeon import Pigeon


class PigeonContainer:
    def __init__(self):
        self._pigeons = []

    def add(self, pigeon: Pigeon):
        self._pigeons.append(pigeon)

    def __getitem__(self, i):
        return self._pigeons[i]

    def __len__(self) -> int:
        return len(self._pigeons)

    @staticmethod
    def to_str(items: List) -> str:
        result = ['pigeons: \n']
        size = len(items)
        if size == 0:
            return 'No pigeons added'
        for index in range(size):
            result.append('{} \n'.format(str(items[index])))
        return ''.join([item for item in result])

    def __str__(self):
        return PigeonContainer.to_str(self._pigeons)

    def sort(self):
        sorted_pigeons = sorted(self._pigeons)
        return PigeonContainer.to_str(sorted_pigeons)

    # def get_permutations(self):
    #     size = len(self._pigeons)
    #     perms = 0
    #
    #     for i in range(size):
    #         for j in range(size - i - 1):
    #             if self._pigeons[j + 1] < self._pigeons[j]:
    #                 temp = self._pigeons[j]
    #                 self._pigeons[j] = self._pigeons[j + 1]
    #                 self._pigeons[j + 1] = temp
    #                 perms += 1
    #     return perms

