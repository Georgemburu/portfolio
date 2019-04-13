from django.urls import path
from .views import (
    connectPageView,
)

urlpatterns = [
    path("",connectPageView, name="connectpage"),
]
