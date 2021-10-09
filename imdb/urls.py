from django.contrib import admin
from django.urls import path, include
from profiles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('', include("movies.urls")),

]
