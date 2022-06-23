from display.models import profile
from django import forms
from django.contrib.auth.models import User
from display.models import Blog
from display.models import File

class UserUpadteForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ["username", "email"]


class ProfileUpdateForm(forms.ModelForm):
    image = forms.ImageField(required=True)
    class Meta:
        model = profile
        fields = ["image"]

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ["author", "title", "description"]

class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ["file"]