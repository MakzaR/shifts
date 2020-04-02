from __future__ import annotations

from src.pigeon import Pigeon


class PigeonContainer:
    def __init__(self):
        self._pigeons = []

    def add(self, pigeon: Pigeon) -> None:
        self._pigeons.append(pigeon)

    def __setitem__(self, key, value) -> None:
        try:
            self._pigeons[key] = value
        except Exception:
            raise IndexError

    def __getitem__(self, key) -> Pigeon:
        if key >= len(self):
            raise IndexError
        return self._pigeons[key]

    def __len__(self) -> int:
        return len(self._pigeons)
