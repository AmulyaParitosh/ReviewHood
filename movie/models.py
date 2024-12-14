import uuid

from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Create your models here.
class Genre(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    name = models.CharField(max_length=127, unique=True)

    def __str__(self) -> str:
        return self.name


class Actor(models.Model):
    class Gender(models.TextChoices):
        MALE = "male", "Male"
        FEMALE = "female", "Female"
        OTHERS = "others", "Others"

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    name = models.CharField(max_length=127, unique=True)
    age = models.IntegerField(validators=[MinValueValidator(0)])
    gender = models.CharField(max_length=7, choices=Gender.choices)

    def __str__(self) -> str:
        return self.name


class Movie(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    name = models.CharField(max_length=127, unique=True)
    rating = models.FloatField(
        validators=[
            MinValueValidator(0.0),
            MaxValueValidator(5.0),
        ]
    )
    release_date = models.DateField()
    genres = models.ManyToManyField(Genre, related_name="movies")
    actors = models.ManyToManyField(Actor, related_name="movies")

    def __str__(self) -> str:
        return self.name


class Review(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="reviews",
    )
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="reviews")
    rating = models.FloatField(
        validators=[
            MinValueValidator(0.0),
            MaxValueValidator(5.0),
        ]
    )
    details = models.TextField(blank=True, default="")
    created_on = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("movie", "user")
