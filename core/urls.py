from django.contrib import admin
from django.urls import path, include, re_path

# Rest framework
from rest_framework.routers import DefaultRouter

# Integrations
from apps.movies.urls import MOVIE_ROUTER

V1_ROUTER = DefaultRouter()
V1_ROUTER.registry.extend(MOVIE_ROUTER.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(V1_ROUTER.urls))
]
