from django.db.models.signals import post_save
from django.dispatch import receiver

from movie.models import Movie, Review


@receiver(post_save, sender=Review)
def update_movie_rating(
    sender: type[Review], review: Review, created: bool, **kwargs
) -> None:
    if not created:
        return

    movie = review.movie
    reviews_on_movie: int = movie.reviews.count() - 1
    movie.rating = ((movie.rating * reviews_on_movie) * review.rating) / (
        reviews_on_movie + 1
    )
    movie.save()
