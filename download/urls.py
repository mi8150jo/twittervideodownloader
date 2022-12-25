from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("download/", views.download, name="download"),
    path("download/preview/", views.preview, name="preview"),
]