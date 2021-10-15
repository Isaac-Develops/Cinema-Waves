from django import forms

from .models import Review

class AddReviewForm(forms.Form):
    text = forms.CharField(widget=forms.TextInput)
    rating = forms.ChoiceField(choices=Review.RATING_CHOICES)  