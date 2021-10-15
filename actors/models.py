from django.db import models

from movies.models import Movie

# Create your models here.
class Actor(models.Model):
    name = models.CharField(max_length=100)
    gender = models.IntegerField()
    image = models.ImageField(
        upload_to='actors', default='assets/default_movie.png')
    biography = models.TextField(null=True, blank=True)
    movies = models.ManyToManyField(Movie)
    birthday = models.DateField()

    def __str__(self):
        return self.name