from django.shortcuts import render

from .models import Review

# Create your views here.
def review_detail_view(request, id):
    review = Review.objects.get(id=id)
    return render(request, 'review_detail.html', {'review': review})