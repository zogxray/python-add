from enum import Enum

class CommandType(Enum):
    TURN = 0
    WALK = 1


class Command(object):

    def __init__(self, type, value):
        self.type = type
        self.value = value
