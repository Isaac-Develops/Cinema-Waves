from django.shortcuts import render,  HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login
from django.views.generic import View

from .models import User
from reviews.models import Review

# Create your views here.
def user_profile_view(request, id):
    user = User.objects.get(id=id)
    reviews = Review.objects.filter(author=user)
    return render(request, 'user_detail.html', {'user': user, 'reviews': reviews})


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

        return render(request, "login.html")
