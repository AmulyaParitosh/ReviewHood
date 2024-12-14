from django.db.models.signals import post_save
from django.dispatch import receiver

from movie.models import Movie, Review


@receiver(post_save, sender=Review)
def update_movie_rating(
    sender: type[Review], instance: Review, created: bool, **kwargs
) -> None:
    movie: Movie = instance.movie
    reviews_on_movie: int = movie.reviews.count() - 1
    if reviews_on_movie == 0:
        movie.rating = instance.rating
    else:
        movie.rating = ((movie.rating * reviews_on_movie) + instance.rating) / (
            reviews_on_movie + 1
        )
    print(movie.rating)
    movie.save()
