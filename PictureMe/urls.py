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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from portfolio.views import index, aboutme, contacts, phototerm, series, photoreports, admin_login

urlpatterns = [
    # path('admin/login/', admin_login),
    # path('admin/', include(admin.site.urls)),
    path('admin/', admin.site.urls, name='admin'),
    # path('admin_login/', admin_login, name='admin_login'),
    path('', index, name="index"),
    path('aboutme/', aboutme, name="aboutme"),
    path('contacts/', contacts, name="contacts"),
    path('phototerm/', phototerm, name="phototerm"),
    path('portfolio/', include("portfolio.urls", namespace="portfolio")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
