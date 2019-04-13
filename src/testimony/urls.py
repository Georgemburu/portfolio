from django.urls import path
from .views import (
    testimonyPageView,
)

urlpatterns = [
    path("",testimonyPageView, name="testimonypage"),
]
