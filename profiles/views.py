from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from profiles.forms import LoginForm

# Create your views here.


def login_view(request):
    context = {}
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=data['password'])
            if user:
                login(request, user)
                return redirect('home')
    form = LoginForm()
    context.update({'form': form})
    return render(request, 'login.html', context)
