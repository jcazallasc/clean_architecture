from typing import TYPE_CHECKING, List

import requests
from bs4 import BeautifulSoup

from janto_events_context.constants import JANTO_FEEDER_URL, JANTO_TIMEOUT
from janto_events_context.infrastructure.tasks import process_janto_event


if TYPE_CHECKING:
    from bs4.element import Tag


class JantoService:

    def __init__(self) -> None:
        self.xml_parser = BeautifulSoup

    def _get_event_data(self, event: "Tag") -> dict:
        _event_details = event.find("event")
        _zones = _event_details.find_all("zone")

        return {
            "base_event_id": event.get("base_event_id"),
            "sell_mode": event.get("sell_mode"),
            "title": event.get("title"),
            "event_start_date": _event_details.get("event_start_date"),
            "event_end_date": _event_details.get("event_end_date"),
            "event_id": _event_details.get("event_id"),
            "sell_from": _event_details.get("sell_from"),
            "sell_to": _event_details.get("sell_to"),
            "sold_out": _event_details.get("sold_out"),
            "zones": [
                {
                    "zone_id": _zone.get("zone_id"),
                    "capacity": _zone.get("capacity"),
                    "price": _zone.get("price"),
                    "name": _zone.get("name"),
                    "numbered": _zone.get("numbered"),
                }
                for _zone in _zones
            ]
        }

    def fetch(self) -> List[int]:
        _response = requests.get(JANTO_FEEDER_URL, timeout=JANTO_TIMEOUT)

        _xml_string = _response.content

        _xml = self.xml_parser(_xml_string)

        _events = _xml.find_all("base_event")

        _base_event_ids = []

        for _event in _events:
            _data = self._get_event_data(_event)

            _base_event_ids.append(_data["base_event_id"])

            process_janto_event.delay(_data)

        return _base_event_ids
