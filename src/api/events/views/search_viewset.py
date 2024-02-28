from rest_framework import status
from rest_framework.views import Response
from rest_framework.viewsets import GenericViewSet

from api.events.serializers.search_request_serializer import SearchRequestSerializer
from events_context.application.event_searcher import EventSearcher


class SearchViewSet(GenericViewSet):

    def search(self, request, *args, **kwargs) -> Response:
        _serializer = SearchRequestSerializer(data=request.query_params.dict())

        if not _serializer.is_valid():
            return Response(
                {
                    "error": _serializer.errors,
                    "data": None,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        _event_entities = EventSearcher()(
            _serializer.validated_data["starts_at"],
            _serializer.validated_data["ends_at"],
        )

        return Response(
            {
                "error": None,
                "data": {
                    "events": [
                        _event_entity.dict()
                        for _event_entity in _event_entities
                    ]
                },
            },
            status=status.HTTP_200_OK,
        )
