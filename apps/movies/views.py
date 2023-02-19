"""
Movies viewset
"""
# Rest framework
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.mixins import (
    ListModelMixin, 
    RetrieveModelMixin,
    DestroyModelMixin,
    UpdateModelMixin
)

# Django
from django.shortcuts import render

# Integrations
from .models import Movies
from .serializer import MovieSerializer

# Create your views here.
class MoviesViewSet(GenericViewSet, ListModelMixin, 
    RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer

    def create(self, request, *args, **kwargs):
        """
        Move create action
        """
        # Add validation for duplicated titles
        try:
            movie_serializer = MovieSerializer(data=request.data)
            movie_serializer.is_valid(raise_exception=True)
            movie = movie_serializer.save()
        except Exception as e:
            error_message = {
                "message": "Error when creating the movie",
                "description": e
            }
            raise ValidationError(error_message)
            
        return Response(
            self.serializer_class(movie).data, 
            status=status.HTTP_201_CREATED
        )
    