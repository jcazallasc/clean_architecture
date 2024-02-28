import abc
from typing import TYPE_CHECKING, Iterable


if TYPE_CHECKING:
    from .event import Event


class PublisherExchange(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def publish(self, event: "Event") -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def publish_all(self, events: Iterable["Event"]) -> None:
        raise NotImplementedError
