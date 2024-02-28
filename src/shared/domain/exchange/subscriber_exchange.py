import abc
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from .consumer import IConsumer


class SubscriberExchange(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def subscribe(self, event_type: str, consumer: 'IConsumer') -> None:
        raise NotImplementedError
