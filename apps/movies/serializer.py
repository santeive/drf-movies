"""
Serializer for movie app
"""

# Rest framework
from rest_framework import serializers
from rest_framework.serializers import ReadOnlyField

# Integrations
from .models import Movies

class MovieSerializer(serializers.ModelSerializer):
    """
    Serializer class for movie model
    """
    class Meta:
        model = Movies
        fields = '__all__'

class MovieCreateSerializer(serializers.ModelSerializer):
    """
    Serializer class for create movie resource
    """

    class meta:
        model = Movies
        fields = '__all__'