from django.shortcuts import (
    render,
    reverse,
    HttpResponseRedirect,
    HttpResponse
)
from django.contrib.auth import (
    authenticate,
    login
)
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.shortcuts import redirect
from .models import User
from reviews.models import Review
from movies.models import Movie
from profiles.forms import UserCreationForm, UserEdit

# Create your views here.


def user_profile_view(request, id):
    user = User.objects.get(id=id)
    reviews = Review.objects.filter(author=user)
    return render(request, 'user_detail.html', {'user': user, 'reviews': reviews})


def all_profiles_view(request):
    profiles = User.objects.all()
    return render(request, 'profiles.html', {'profiles': profiles})


@login_required
def watchlist_view(request, id):
    user = request.user
    movie = Movie.objects.get(id=id)
    if movie in user.watched_movies.all():
        user.watched_movies.remove(movie)
    user.watchlist.add(movie)
    return HttpResponseRedirect(reverse('movies', args=(id,)))


@login_required
def watched_list_view(request, id):
    user = request.user
    movie = Movie.objects.get(id=id)
    if movie in user.watchlist.all():
        user.watchlist.remove(movie)
    user.watched_movies.add(movie)
    return HttpResponseRedirect(reverse('movies', args=(id,)))


@login_required
def remove_watchlist_view(request, id):
    user = request.user
    movie = Movie.objects.get(id=id)
    user.watchlist.remove(movie)
    return HttpResponseRedirect(reverse('movies', args=(id,)))


@login_required
def remove_watchedlist_view(request, id):
    user = request.user
    movie = Movie.objects.get(id=id)
    user.watched_movies.remove(movie)
    return HttpResponseRedirect(reverse('movies', args=(id,)))


def user_edit(request, id):
    user = User.objects.get(id=id)
    if request.method == 'POST':
        form = UserEdit(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user.about = data['about']
            user.save()
            return render(request, 'user_detail.html')
    form = UserEdit()
    return render(request, 'registration/edit_profile.html', {'form': form})


class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'registration/register_user.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            User.objects.create_user(username=username, password=password)
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')


class LoginView(View):
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)

                return HttpResponseRedirect('/form')
            else:
                return HttpResponse("Inactive user.")
        else:
            return HttpResponseRedirect("LOGIN_URL")
