import math
from django.shortcuts import (
    redirect,
    render,
    # reverse,
    # HttpResponseRedirect,
    # HttpResponse
)
from .models import BannerCards, Cards
from django.contrib.auth.models import auth
from .models import Movie
from reviews.models import Review
from actors.models import Actor

# Create your views here.


def movie_detail_view(request, id):
    movie = Movie.objects.get(id=id)
    reviews = Review.objects.filter(movie=movie)
    average_rating = 0
    if reviews.count() != 0:
        for review in reviews:
            average_rating += review.rating
        average_rating = math.floor((average_rating / reviews.count()) * 10) / 10
    cast = movie.actor_set.all()
    return render(request, 'movie_detail.html', {'movie': movie, 'reviews': reviews, 'cast': cast, 'average_rating': average_rating})


def all_movies_view(request):
    movies = Movie.objects.all()
    return render(request, "movies.html", {'movies': movies})


def home(request):
    bannerCards = BannerCards.objects.all()
    cards = Cards.objects.all()
    context = {
        'bannerCards': bannerCards,
        'cards': cards,
    }
    return render(request, "Home/home.html", context)


def search(request):
    query = request.GET['query']
    movies = Movie.objects.filter(title__icontains=query)
    actors = Actor.objects.filter(name__icontains=query)
    context = {
        'movies': movies,
        "actors": actors,
        "query": query
    }
    return render(request, "Home/search.html", context)


def logout(request):
    auth.logout(request)
    return redirect("/")


def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)


def server_error_view(request):
    return render(request, '500.html', status=500)
