from django.db import models

# Create your models here.

from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Genre(models.Model):
    genre_name = models.CharField(max_length=100)

    def __str__(self):
        return self.genre_name

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE,)
    genres = models.ManyToManyField(Genre)
    

    def __str__(self):
        return self.title

class MovieDetail(models.Model):
    movie = models.OneToOneField(Movie, on_delete=models.CASCADE)
    release_date = models.DateField()
    duration = models.IntegerField(help_text="Duration in minutes")
    budget = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.movie     