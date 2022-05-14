from django.urls import path

from .views import FileCheckAPIView

app_name = "file_checker"

urlpatterns = [
    path("", FileCheckAPIView.as_view()),
]
