from django.shortcuts import render

from .models import Actor

# Create your views here.
def actor_detail_view(request, id):
    actor = Actor.objects.get(id=id)
    return render(request, 'actor_detail.html', {'actor': actor})

def all_actors_view(request):
    actors = Actor.objects.all()
    return render(request, 'actors.html', {'actors': actors})