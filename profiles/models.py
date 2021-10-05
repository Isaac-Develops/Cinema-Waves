from django.db import models
from django.contrib.auth.models import AbstractUser

from movies.models import Movie

# Create your models here.
class User(AbstractUser):
    about = models.TextField(null=True, blank=True)
    seen_movies = models.ManyToManyField(Movie, related_name='seen')
    want_to_see_movies = models.ManyToManyField(Movie, related_name='want_to_see')