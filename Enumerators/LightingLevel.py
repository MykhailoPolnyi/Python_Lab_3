from enum import Enum


class LightingLevel(Enum):
    DARK = 1
    MEDIUM = 2
    BRIGHT = 3

    def __str__(self):
        return self.name
