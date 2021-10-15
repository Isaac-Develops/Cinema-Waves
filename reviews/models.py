from django.db import models

from profiles.models import User
from movies.models import Movie

# Create your models here.
class Review(models.Model):
    
    # class Rating(models.IntegerChoices):
    #     ONE_STAR = 1
    #     TWO_STARS = 2
    #     THREE_STARS = 3
    #     FOUR_STARS = 4
    #     FIVE_STARS = 5

    ONE_STAR = 1
    TWO_STARS = 2
    THREE_STARS = 3
    FOUR_STARS = 4
    FIVE_STARS = 5
    RATING_CHOICES = (
        (ONE_STAR, 'One Star'),
        (TWO_STARS, 'Two Stars'),
        (THREE_STARS, 'Three Stars'),
        (FOUR_STARS, 'Four Stars'),
        (FIVE_STARS, 'Five Stars')
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES, default=FIVE_STARS)
    text = models.TextField()