from django.urls import path

from api.check.views.check_viewset import CheckViewSet


app_name = "check"
urlpatterns = [
    path("", CheckViewSet.as_view({"get": "check"}), name="check"),
]
