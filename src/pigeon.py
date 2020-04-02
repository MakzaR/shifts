class Pigeon:
    def __init__(self, index: int, velocity: int):
        self.index = index
        self.velocity = velocity

    def __eq__(self, other) -> bool:
        if isinstance(other, Pigeon):
            return self.__dict__ == other.__dict__
        return False

    def __lt__(self, other) -> bool:
        return self.velocity < other.velocity
