from celery import shared_task

from janto_events_context.application.janto_event_processor import JantoEventProcessor


@shared_task
def process_janto_event(event_data: dict) -> None:
    JantoEventProcessor()(event_data)
