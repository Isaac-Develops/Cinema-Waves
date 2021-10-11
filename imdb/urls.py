from django.contrib import admin
from django.urls import path, include
from profiles import views
from django.contrib.auth.views import LoginView

from profiles.views import user_profile_view
from reviews.views import review_detail_view, CreateReviewView
from movies.views import movie_detail_view
from actors.views import actor_detail_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/<int:id>/', user_profile_view, name='profiles'),
    path('reviews/<int:id>/', review_detail_view, name='reviews'),
    path('reviews/create/<int:id>/', CreateReviewView.as_view(), name='create_review'),
    path('movies/<int:id>/', movie_detail_view, name='movies'),
    path('actors/<int:id>/', actor_detail_view, name='actors'),
    path('login/', LoginView.as_view(), name='login'),
    path('', include("movies.urls")),

]
