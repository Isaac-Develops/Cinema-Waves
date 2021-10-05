from django.db import models
from django.contrib.auth.models import AbstractUser

from movies.models import Movie

# Create your models here.
class User(AbstractUser):
    about = models.TextField(null=True, blank=True)
    watched_movies = models.ManyToManyField(Movie, related_name='watched_movies')
    watchlist = models.ManyToManyField(Movie, related_name='watchlist')