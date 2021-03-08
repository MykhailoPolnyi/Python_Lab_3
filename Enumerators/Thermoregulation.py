from enum import Enum


class ThermoregulationType(Enum):
    WARM_BLOODED = 1
    COLD_BLOODED = 2

    def __str__(self):
        return self.name
