from enum import Enum


class BaseEnum(Enum):
    @classmethod
    def choices(cls) -> tuple:
        return tuple((status.value, status.name) for status in cls)
