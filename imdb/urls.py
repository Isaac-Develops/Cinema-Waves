from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView
from reviews import views as rview
from movies import views as mview
from actors import views as aview
from profiles import views as pview

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", mview.home, name="home"),
    path('users/<int:id>/', pview.user_profile_view, name='profiles'),
    path('users/watchlist/add/<int:id>/',
         pview.watchlist_view, name='watchlist'),
    path('users/watchedlist/add/<int:id>',
         pview.watched_list_view, name='watched_list'),
    path('users/watchlist/remove/<int:id>/',
         pview.remove_watchlist_view, name='watchlist_remove'),
    path('users/watchedlist/remove/<int:id>/',
         pview.remove_watchedlist_view, name='watched_list_remove'),
    path('reviews/<int:id>/', rview.review_detail_view, name='reviews'),
    path('reviews/create/<int:id>/',
         rview.CreateReviewView.as_view(), name='create_review'),
    path('movies/<int:id>/', mview.movie_detail_view, name='movies'),
    path('actors/<int:id>/', aview.actor_detail_view, name='actors'),
    path('login/', LoginView.as_view(), name='login'),
    path("search/", mview.search, name="search"),
    path("logout/", mview.logout, name="logout"),
    path('register/', pview.register_user, name='register')
]

handler404 = 'movies.views.page_not_found_view'
handler500 = 'movies.views.server_error_view'
