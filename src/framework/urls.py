from django.urls import path
from .views import (
    frameworkPageView
)


urlpatterns = [
    path('',frameworkPageView.as_view(),name="frameworkpage"),
    
]
