"""
URL configuration for PictureMe project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from portfolio.views import (
    RobotsView,
    aboutme,
    contacts,
    index,
    phototerm,
)

urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    path("robots.txt", RobotsView.as_view()),
    path("", index, name="index"),
    path("aboutme/", aboutme, name="aboutme"),
    path("contacts/", contacts, name="contacts"),
    path("phototerm/", phototerm, name="phototerm"),
    path("portfolio/", include("portfolio.urls", namespace="portfolio")),
    path("", include("django_prometheus.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
