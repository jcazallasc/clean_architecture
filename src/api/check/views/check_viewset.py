from rest_framework import status
from rest_framework.views import Response
from rest_framework.viewsets import GenericViewSet


class CheckViewSet(GenericViewSet):

    def check(self, request, *args, **kwargs) -> Response:
        return Response({}, status=status.HTTP_200_OK)
