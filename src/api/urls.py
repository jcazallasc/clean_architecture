from django.urls import include, path


app_name = "api"
urlpatterns = [
    path("check/", include("api.check.urls", namespace="check")),
    path("events/", include("api.events.urls", namespace="events")),
]
