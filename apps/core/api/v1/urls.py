from django.urls import include, path

app_name = "v1"

urlpatterns = [
    path("auth/", include("dj_rest_auth.urls")),
    path("file-checker/", include("apps.api.file_checker.v1")),
]
