class Pigeon:
    def __init__(self, index: int, velocity: int):
        self.index = index
        self.velocity = velocity

    def __eq__(self, other) -> bool:
        self_dict = self.__dict__
        other_dict = other.__dict__
        if type(other) is not Pigeon or len(self_dict) != len(other_dict):
            return False
        if self_dict != other_dict:
            return False
        return True

    def __lt__(self, other):
        return self.velocity < other.velocity

    def __str__(self) -> str:
        return 'index: {}, velocity: {}'.format(self.index, self.velocity)
