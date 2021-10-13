from django.db import models
from django.utils.text import slugify
from django.utils import timezone

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
    image = models.ImageField(
        upload_to='movies', default='assets/default_movie.png')
    category = models.CharField(
        choices=CATEGORY_CHOICES, max_length=1, default=ACTION)
    language = models.CharField(
        choices=LANGUAGES_CHOICES, max_length=2, default=ENGLISH)
    status = models.CharField(choices=STATUS_CHOICES,
                              max_length=2, default=RECENTLY_ADDED)
    year_of_production = models.DateField()
    views_count = models.IntegerField(default=0)

    created = models.DateTimeField(default=timezone.now)

    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Movie, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


LINK_CHOICES = (
    ('D', 'DOWNLOAD LINK'),
    ('W', 'WATCH LINK'),
)


class MovieLinks(models.Model):
    movie = models.ForeignKey(
        Movie, related_name='movie_watch_link', on_delete=models.CASCADE)
    type = models.CharField(choices=LINK_CHOICES, max_length=1)
    link = models.URLField()

    def __str__(self):
        return str(self.movie)


class BannerCards(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    content = models.TextField()
    imageurl = models.CharField(max_length=1000)
    targetUrl = models.CharField(max_length=1000)

    def __str__(self):
        return self.title


class Cards(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    imageurl = models.CharField(max_length=1000)
    targetUrl = models.CharField(max_length=1000)

    def __str__(self):
        return self.title
