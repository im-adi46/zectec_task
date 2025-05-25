from django import forms
from .models import Director, Genre, Movie, MovieDetail

class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = ['name']

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['genre_name']

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'director', 'genres']
        widgets = {
            'genres': forms.CheckboxSelectMultiple()
        }

class MovieDetailForm(forms.ModelForm):
    class Meta:
        model = MovieDetail
        fields = ['movie', 'release_date', 'duration', 'budget']
