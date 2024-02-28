from django.db import models

from shared.domain.enums.janto_event_status import JantoEventStatus


class JantoEvent(models.Model):
    base_event_id = models.IntegerField()
    event_id = models.IntegerField()
    title = models.CharField(max_length=500)
    sell_mode = models.CharField(max_length=20)
    event_start_date = models.DateTimeField()
    event_end_date = models.DateTimeField(null=True)
    sell_from = models.DateTimeField()
    sell_to = models.DateTimeField()
    sold_out = models.BooleanField()
    zones = models.JSONField(default=dict)
    status = models.IntegerField(choices=JantoEventStatus.choices(), default=JantoEventStatus.Active.value)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=["event_id"]),
            models.Index(fields=["base_event_id"]),
        ]
