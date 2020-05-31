"""morning_library_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path


from django.contrib import admin
from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from morning_library_app.morning_library.views import LibraryEntryViewSet, TrackViewSet

router = DefaultRouter()
router.register('libraryentry', LibraryEntryViewSet)
router.register('track', TrackViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url('^api/', include((router.urls, "libraryentry"))),
    url('^api/', include((router.urls, "track"))),
]
