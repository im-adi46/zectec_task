from django.urls import path
from . import views
from .views import*

urlpatterns = [
    # Director URLs
    path('directors/', views.director_list, name='director_list'),
    path('directors/add/', views.director_create, name='director_create'),
    path('directors/<int:pk>/edit/', views.director_update, name='director_update'),
    path('directors/<int:pk>/delete/', views.director_delete, name='director_delete'),

    # Movie URLs
    path('', views.movie_list, name='movie_list'),
    path('movies/add/', views.movie_create, name='movie_create'),
    path('movies/<int:pk>/edit/', views.movie_update, name='movie_update'),
    path('movies/<int:pk>/delete/', views.movie_delete, name='movie_delete'),

      path('genres/', genre_list, name='genre_list'),
    path('genres/add/', genre_create, name='genre_create'),
    path('genres/<int:pk>/edit/', genre_update, name='genre_update'),
    path('genres/<int:pk>/delete/', genre_delete, name='genre_delete'),
    
]
