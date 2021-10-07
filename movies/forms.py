from django.db import forms
from movies.models import Movie


class Form(forms.ModelForm):
    
    class Meta:
        model = Movie
        fields = (
                  "title",
                  'year_of_production',
                  'language',
                  'category'
                  )

