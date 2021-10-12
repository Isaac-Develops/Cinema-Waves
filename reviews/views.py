from django.shortcuts import render, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from movies.models import Movie
from .models import Review
from .forms import AddReviewForm

# Create your views here.
def review_detail_view(request, id):
    review = Review.objects.get(id=id)
    return render(request, 'review_detail.html', {'review': review})

class CreateReviewView(LoginRequiredMixin, View):
    template_name = 'create_review.html'

    def get(self, request, id):
        form = AddReviewForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, id):
        form = AddReviewForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            movie = Movie.objects.get(id=id)
            review = Review.objects.create(
                author=request.user,
                movie=movie,
                rating=data.get('rating'),
                text=data.get('text')
                )
            return redirect(reverse('movies', args=(id,)))