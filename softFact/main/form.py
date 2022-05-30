from django import forms
from django.forms import ModelForm
from .models import Movies, Movie


class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'comment')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control'}),
        }