from django.http import JsonResponse
from rest_framework import status


def custom_400(*_, **__):  # pragma: no cover
    return JsonResponse({"error": "Bad request"}, status=status.HTTP_400_BAD_REQUEST)


def custom_403(*_, **__):  # pragma: no cover
    return JsonResponse({"error": "Forbidden"}, status=status.HTTP_403_FORBIDDEN)


def custom_404(*_, **__):  # pragma: no cover
    return JsonResponse({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)


def custom_500(*_, **__):  # pragma: no cover
    return JsonResponse({"error": "Internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
