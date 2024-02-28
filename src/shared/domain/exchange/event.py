import abc
import uuid
from datetime import datetime

import inject
from pydantic import BaseModel, Field

from shared.domain.exchange.event_attributes import EventAttributes
from shared.domain.exchange.publisher_exchange import PublisherExchange


class Event(BaseModel, abc.ABC):

    attributes: EventAttributes
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    occurred_on: datetime = Field(default_factory=datetime.utcnow)
    meta: dict = Field(default_factory=dict)
    type: str

    class Config:
        allow_mutation = False

    def get_attributes(self) -> dict:
        return self.attributes.dict()

    def to_dict(self) -> dict:
        return {
            "data": {
                "id": self.id.hex,
                "type": self.type,
                "occurred_on": self.occurred_on.isoformat(),
                "attributes": self.get_attributes(),
                "meta": self.meta,
            }
        }

    def publish(self):
        exchange = inject.instance(PublisherExchange)

        exchange.publish(self)
