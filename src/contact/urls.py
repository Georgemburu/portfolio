from django.urls import path
from .views import contactPageView


urlpatterns = [
    path("",contactPageView,name="contactpage"),
]
