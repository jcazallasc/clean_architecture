from uuid import uuid4

from django.db import models

from shared.domain.enums import EventProvider, EventStatus


class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    original_id = models.CharField(max_length=500)
    provider = models.IntegerField(choices=EventProvider.choices())
    title = models.CharField(max_length=500)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True)
    min_price = models.FloatField(null=True)
    max_price = models.FloatField(null=True)
    status = models.IntegerField(choices=EventStatus.choices(), default=EventStatus.PendingReview.value)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=["original_id"]),
            models.Index(fields=["provider"]),
            models.Index(fields=["original_id", "provider"]),
            models.Index(fields=["start_date", "end_date"]),
        ]
