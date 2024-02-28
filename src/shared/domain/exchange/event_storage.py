import abc
from typing import TYPE_CHECKING, List


if TYPE_CHECKING:
    from shared.domain.exchange.event import Event


class EventStorage(metaclass=abc.ABCMeta):

    def record(self, event: "Event") -> None:
        raise NotImplementedError

    def pull_events(self) -> List["Event"]:
        raise NotImplementedError
