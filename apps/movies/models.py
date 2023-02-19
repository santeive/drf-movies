from django.db import models

# Create your models here.
class Movies(models.Model):
    """
    Model for Movies
    """
    title = models.CharField(
        max_length=100,
        help_text="Title assgned to the movie"
    )
    description = models.CharField(
        max_length=250,
        help_text="Movie's description"
    )
    image = models.CharField(
        max_length=250,
        help_text="Image for the movie"
    )
    stock = models.IntegerField()
    rental_price = models.FloatField()
    sale_price = models.FloatField()
    availability = models.BooleanField()