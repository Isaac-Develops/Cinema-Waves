from django.db import models

from profiles.models import User
from movies.models import Movie

# Create your models here.
class Review(models.Model):
    
    class Raiting(models.IntegerChoices):
        ONE_STAR = 1
        TWO_STARS = 2
        THREE_STARS = 3
        FOUR_STARS = 4
        FIVE_STARS = 5

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    raiting = models.IntegerField(choices=Raiting.choices)
    text = models.TextField()