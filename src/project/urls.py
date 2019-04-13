from django.urls import path
from .views import (
    projectViewPage
)


urlpatterns = [
    path("",projectViewPage, name="projectviewpage")
]
