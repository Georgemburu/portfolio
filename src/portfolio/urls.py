"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from home import urls as home_urls
from framework import urls as framework_urls
from project import urls as project_urls
from testimony import urls as testimony_urls
from contact import urls as contact_urls
from connect import urls as connect_urls

urlpatterns = [
     path('',include(home_urls)),
     path('skill/<slug>/',include(framework_urls)),
     path('skill/<slug>/<string>/',include(project_urls)),
     path('testimonials/',include(testimony_urls)),
     path('contact/',include(contact_urls)),
     path('connect/',include(connect_urls)),
     path('admin/', admin.site.urls),
   
]+static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)