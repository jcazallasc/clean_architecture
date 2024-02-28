import abc


class Consumer(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def consume(self, event_id: str, event_type: str, attributes: dict) -> None:
        raise NotImplementedError
