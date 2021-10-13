from django.contrib import admin
from .models import BannerCards, Cards
from .models import Movie


# Register your models here.
admin.site.register(Movie)
admin.site.register(BannerCards)
admin.site.register(Cards)
