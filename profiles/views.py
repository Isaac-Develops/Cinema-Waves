from django.shortcuts import render
from profiles.models import User
from reviews.models import Review

# Create your views here.
def user_profile_view(request, id):
    user = User.objects.get(id=id)
    reviews = Review.objects.filter(author=user)
    return render(request, 'user_detail.html', {'user': user, 'reviews': reviews})