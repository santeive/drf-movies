"""
Movie app url
"""

# Django
from django.urls import path
from .views import MoviesViewSet

# rest framework
from rest_framework.routers import SimpleRouter

MOVIE_ROUTER = SimpleRouter()
MOVIE_ROUTER.register(r'movies', MoviesViewSet, basename='movies')