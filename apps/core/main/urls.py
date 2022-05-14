from django.urls import include, path

urlpatterns = [
    path("api/", include("apps.core.api.urls"), name="api"),
]
