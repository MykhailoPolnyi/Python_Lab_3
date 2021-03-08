from enum import Enum


class SortOrder(Enum):
    ASC = 0
    DESC = 1

    def __str__(self):
        return "Order type: {type}, Value: {value}".format(type=self.name, value=self.value)
