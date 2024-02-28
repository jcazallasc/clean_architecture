from shared.domain.enums.base_enum import BaseEnum


class EventStatus(BaseEnum):
    Inactive = 0
    Active = 1
    PendingReview = 2
