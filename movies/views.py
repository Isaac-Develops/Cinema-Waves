from django.shortcuts import render
from movies.models import Movie

# Create your views here.
def movie(request):
    context = {
        'movie': Movie.objects.all().order_by('title'),
        'year_of_production': Movie.year_of_production,
        'image': Movie.image,
        'description': Movie.description,
        }
    return render(request, 'home.html', context)

