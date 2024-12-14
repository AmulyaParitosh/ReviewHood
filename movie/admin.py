from django.contrib import admin

from movie.models import Actor, Genre, Movie, Review

# Register your models here.


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ("name", "age", "gender")


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("name", "rating", "release_date")
    list_filter = ("genres", "actors")
    filter_horizontal = ("genres", "actors")


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "movie", "rating", "details", "created_on")
    list_filter = ("user", "movie", "rating")
