from datetime import datetime
from typing import List

from pydantic import BaseModel

from shared.domain.enums.event_provider import EventProvider


class JantoEventEntity(BaseModel):
    base_event_id: int
    event_id: str
    title: str
    sell_mode: str
    event_start_date: datetime
    event_end_date: datetime
    sell_from: datetime
    sell_to: datetime
    sold_out: bool
    zones: List[dict] = {}

    class Config:
        orm_mode = True

    def _get_prices(self) -> List[float]:
        return [
            _zone["price"]
            for _zone in self.zones
        ]

    def get_min_price(self) -> float:
        return min(self._get_prices())

    def get_max_price(self) -> float:
        return max(self._get_prices())

    def normalize(self) -> dict:
        return {
            "original_id": self.base_event_id,
            "provider": EventProvider.Janto.value,
            "title": self.title,
            "start_date": self.event_start_date.date(),
            "end_date": self.event_end_date.date(),
            "min_price": self.get_min_price(),
            "max_price": self.get_max_price(),
        }
