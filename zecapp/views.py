
# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Director, Genre, Movie, MovieDetail
from .forms import DirectorForm, GenreForm, MovieForm, MovieDetailForm

# ---------- Director Views ----------
def director_list(request):
    directors = Director.objects.all()
    return render(request, 'movies/director_list.html', {'directors': directors})

def director_create(request):
    form = DirectorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('director_list')
    return render(request, 'movies/form.html', {'form': form, 'title': 'Add Director'})

def director_update(request, pk):
    director = get_object_or_404(Director, pk=pk)
    form = DirectorForm(request.POST or None, instance=director)
    if form.is_valid():
        form.save()
        return redirect('director_list')
    return render(request, 'movies/form.html', {'form': form, 'title': 'Edit Director'})

def director_delete(request, pk):
    director = get_object_or_404(Director, pk=pk)
    if request.method == 'POST':
        director.delete()
        return redirect('director_list')
    return render(request, 'movies/confirm_delete.html', {'object': director})


# ---------- Movie Views ----------
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/movie_list.html', {'movies': movies})

def movie_create(request):
    form = MovieForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('movie_list')
    return render(request, 'movies/form.html', {'form': form, 'title': 'Add Movie'})

def movie_update(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    form = MovieForm(request.POST or None, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('movie_list')
    return render(request, 'movies/form.html', {'form': form, 'title': 'Edit Movie'})

def movie_delete(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        movie.delete()
        return redirect('movie_list')
    return render(request, 'movies/confirm_delete.html', {'object': movie})

# ✅ List View
def genre_list(request):
    genres = Genre.objects.all()
    return render(request, 'movies/genre_list.html', {'genres': genres})

# ✅ Create View
def genre_create(request):
    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('genre_list')
    else:
        form = GenreForm()
    return render(request, 'movies/form.html', {'form': form, 'title': 'Add Genre'})

# ✅ Update View
def genre_update(request, pk):
    genre = get_object_or_404(Genre, pk=pk)
    if request.method == 'POST':
        form = GenreForm(request.POST, instance=genre)
        if form.is_valid():
            form.save()
            return redirect('genre_list')
    else:
        form = GenreForm(instance=genre)
    return render(request, 'movies/form.html', {'form': form, 'title': 'Edit Genre'})

# ✅ Delete View
def genre_delete(request, pk):
    genre = get_object_or_404(Genre, pk=pk)
    if request.method == 'POST':
        genre.delete()
        return redirect('genre_list')
    return render(request, 'movies/confirm_delete.html', {'object': genre, 'title': 'Delete Genre'})

