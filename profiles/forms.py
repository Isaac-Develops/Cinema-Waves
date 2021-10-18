from django import forms
from profiles.models import User


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            "username",
            "password",
            )


class UserCreationForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)


class UserEdit(forms.Form):
    about = forms.CharField(max_length=200)


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
