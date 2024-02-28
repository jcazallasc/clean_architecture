from django.urls import path

from api.events.views.search_viewset import SearchViewSet


app_name = "events"
urlpatterns = [
    path("search/", SearchViewSet.as_view({"get": "search"}), name="search"),
]
