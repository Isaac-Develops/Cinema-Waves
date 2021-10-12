from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView

from profiles.views import (
    user_profile_view,
    watched_list_view,
    watchlist_view,
    remove_watchedlist_view,
    remove_watchlist_view
    )
from reviews.views import review_detail_view, CreateReviewView
from movies.views import movie_detail_view
from actors.views import actor_detail_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/<int:id>/', user_profile_view, name='profiles'),
    path('users/watchlist/add/<int:id>/', watchlist_view, name='watchlist'),
    path('users/watchedlist/add/<int:id>', watched_list_view, name='watched_list'),
    path('users/watchlist/remove/<int:id>/', remove_watchlist_view, name='watchlist_remove'),
    path('users/watchedlist/remove/<int:id>/', remove_watchedlist_view, name='watched_list_remove'),
    path('reviews/<int:id>/', review_detail_view, name='reviews'),
    path('reviews/create/<int:id>/', CreateReviewView.as_view(), name='create_review'),
    path('movies/<int:id>/', movie_detail_view, name='movies'),
    path('actors/<int:id>/', actor_detail_view, name='actors'),
    path('login/', LoginView.as_view(), name='login'),
    path('', include("movies.urls")),
]
