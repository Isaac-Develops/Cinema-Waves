from django.db import models

# Create your models here.
class Movie(models.Model):
    ACTION = 'AC'
    DRAMA = 'DR'
    COMEDY = 'CO'
    ROMANCE = 'RO'
    CATEGORY_CHOICES = [
        ('A', 'Action'),
        ('D', 'Drama'),
        ('C', 'Comedy'),
        ('R', 'Romance'),
    ]

    ENGLISH = 'EN'
    GERMAN = 'GR'
    FRENCH = 'FR'
    LANGUAGES_CHOICES = [
        ('EN', 'English'),
        ('GR', 'German'),
        ('FR', 'French')
    ]

    RECENTLY_ADDED = 'RA'
    MOST_WATCHED = 'MW'
    TOP_RATED = 'TR'
    STATUS_CHOICES = [
        ('RA', 'Recently Added'),
        ('MW', 'Most Watched'),
        ('TR', 'Top Rated')
    ]

    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, null=True, blank=True)
    image = models.ImageField(upload_to='movies', default='assets/default_movie.png')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=1, default=ACTION)
    language = models.CharField(choices=LANGUAGES_CHOICES, max_length=2, default=ENGLISH)
    status = models.CharField(choices=STATUS_CHOICES, max_length=2, default=RECENTLY_ADDED)
    year_of_production = models.DateField()
    views_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title
