from django import forms

class AddReviewForm(forms.Form):
    text = forms.CharField(widget=forms.TextInput)
    rating = forms.IntegerField()