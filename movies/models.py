from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    release_date = models.DateField()
    overview = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name