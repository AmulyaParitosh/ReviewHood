"""
URL configuration for ReviewHood project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from movie.views import (
    ActorDetailView,
    ActorListCreateView,
    GenreDetailView,
    GenreListCreateView,
    MovieDetailView,
    MovieListCreateView,
    MoviesByActorListView,
    MoviesByGenreListView,
)

urlpatterns = [
    path("admin", admin.site.urls),
    path(
        "api/actors",
        ActorListCreateView.as_view(),
        name="list-create-actors",
    ),
    path(
        "api/actors/<str:pk>",
        ActorDetailView.as_view(),
        name="view-update-delete-actor",
    ),
    path(
        "api/actors/<str:pk>/movies",
        MoviesByActorListView.as_view(),
        name="list-movies-by-actor",
    ),
    path(
        "api/genres",
        GenreListCreateView.as_view(),
        name="list-create-genres",
    ),
    path(
        "api/genres/<str:pk>",
        GenreDetailView.as_view(),
        name="view-update-delete-genre",
    ),
    path(
        "api/genres/<str:pk>/movies",
        MoviesByGenreListView.as_view(),
        name="list-movies-by-genre",
    ),
    path(
        "api/movies",
        MovieListCreateView.as_view(),
        name="list-create-movies",
    ),
    path(
        "api/movies/<str:pk>",
        MovieDetailView.as_view(),
        name="view-update-delete-movies",
    ),
]
