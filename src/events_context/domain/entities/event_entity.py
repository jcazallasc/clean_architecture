from datetime import datetime
from uuid import UUID

from pydantic import BaseModel

from shared.domain.enums import EventStatus


class EventEntity(BaseModel):
    id: UUID
    original_id: str
    provider: str
    title: str
    start_date: datetime
    end_date: datetime
    min_price: float
    max_price: float
    status: EventStatus

    class Config:
        orm_mode = True

    def dict(self) -> dict:
        return {
            "id": str(self.id),
            "title": self.title,
            "start_date": self.start_date.date(),
            "start_time": self.start_date.time(),
            "end_date": self.end_date.date(),
            "end_time": self.end_date.time(),
            "min_price": self.min_price,
            "max_price": self.max_price,
        }
