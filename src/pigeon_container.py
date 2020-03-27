from __future__ import annotations

from typing import List

from src.pigeon import Pigeon


class PigeonContainer:
    def __init__(self, pigeons: List = None):
        if not pigeons:
            self._pigeons: List[Pigeon] = []
        else:
            self._pigeons = pigeons

    def add(self, pigeon: Pigeon) -> None:
        self._pigeons.append(pigeon)

    def __setitem__(self, key, value) -> None:
        self._pigeons[key] = value

    def __getitem__(self, key) -> Pigeon:
        return self._pigeons[key]

    def __len__(self) -> int:
        return len(self._pigeons)

    def __str__(self) -> str:
        result = ['pigeons: \n']
        size = len(self._pigeons)
        if size == 0:
            return 'No pigeons added'
        for index in range(size):
            result.append('{} \n'.format(str(self._pigeons[index])))
        return ''.join(result)

    def sort(self) -> PigeonContainer:
        sorted_pigeons = sorted(self._pigeons)
        return PigeonContainer(sorted_pigeons)
