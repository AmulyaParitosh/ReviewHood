from typing import Optional

from django.db.models.manager import BaseManager
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from movie.models import Actor, Genre, Movie, Review
from movie.serializers import (
    ActorSerializer,
    GenreSerializer,
    MovieSerializer,
    ReviewSerializer,
)


class ActorListCreateView(APIView):

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        elif self.request.method == "POST":
            return [IsAdminUser()]

        return super().get_permissions()

    def get(self, request: Request) -> Response:
        actors: BaseManager[Actor] = Actor.objects.all()
        paginator = LimitOffsetPagination()
        paginated_genre: Optional[list[Actor]] = paginator.paginate_queryset(
            actors, request
        )
        serializer = ActorSerializer(paginated_genre, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request: Request) -> Response:
        serializer = ActorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ActorDetailView(APIView):

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        elif self.request.method in ("PUT", "DELETE"):
            return [IsAdminUser()]

        return super().get_permissions()

    def get(self, request: Request, pk: str) -> Response:
        try:
            actor: Actor = Actor.objects.get(id=pk)
        except Actor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ActorSerializer(actor)
        return Response(serializer.data)

    def put(self, request: Request, pk: str) -> Response:
        try:
            actor: Actor = Actor.objects.get(id=pk)
        except Actor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ActorSerializer(actor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, pk: str) -> Response:
        try:
            actor: Actor = Actor.objects.get(id=pk)
        except Actor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        actor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MoviesByActorListView(ListAPIView):
    serializer_class = MovieSerializer
    permission_classes = [AllowAny]

    def get_queryset(self) -> BaseManager[Movie]:
        actor_id: str = self.kwargs.get("pk")  # Retrieve actor_id from URL
        try:
            actor: Actor = Actor.objects.get(id=actor_id)
        except Actor.DoesNotExist:
            raise NotFound("Actor not found")
        return actor.movies.all()


class GenreListCreateView(APIView):

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        elif self.request.method == "POST":
            return [IsAdminUser()]

        return super().get_permissions()

    def get(self, request: Request) -> Response:
        genre: BaseManager[Genre] = Genre.objects.all()
        paginator = LimitOffsetPagination()
        paginated_genre: Optional[list[Genre]] = paginator.paginate_queryset(
            genre, request
        )
        serializer = GenreSerializer(paginated_genre, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request: Request) -> Response:
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GenreDetailView(APIView):

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        elif self.request.method in ("PUT", "DELETE"):
            return [IsAdminUser()]

        return super().get_permissions()

    def get(self, request: Request, pk: str) -> Response:
        try:
            genre: Genre = Genre.objects.get(id=pk)
        except Genre.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = GenreSerializer(genre)
        return Response(serializer.data)

    def put(self, request: Request, pk: str) -> Response:
        try:
            genre: Genre = Genre.objects.get(id=pk)
        except Genre.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = GenreSerializer(genre, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, pk: str) -> Response:
        try:
            genre: Genre = Genre.objects.get(id=pk)
        except Genre.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MoviesByGenreListView(ListAPIView):
    serializer_class = MovieSerializer
    permission_classes = [AllowAny]

    def get_queryset(self) -> BaseManager[Movie]:
        genre_id = self.kwargs.get("pk")
        try:
            genre = Genre.objects.get(id=genre_id)
        except Genre.DoesNotExist:
            raise NotFound("Genre not found")
        return genre.movies.all()


class MovieListCreateView(APIView):

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        elif self.request.method == "POST":
            return [IsAdminUser()]

        return super().get_permissions()

    def get(self, request: Request) -> Response:
        movies: BaseManager[Movie] = Movie.objects.all()
        paginator = LimitOffsetPagination()
        paginated_movies: Optional[list[Movie]] = paginator.paginate_queryset(
            movies, request
        )
        serializer = MovieSerializer(paginated_movies, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request: Request) -> Response:
        movie_data = request.data
        movie_data["rating"] = 0
        serializer = MovieSerializer(data=movie_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieDetailView(RetrieveUpdateDestroyAPIView):

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        elif self.request.method in ("PUT", "DELETE"):
            return [IsAdminUser()]

        return super().get_permissions()

    def get(self, request: Request, pk: str) -> Response:
        try:
            movie: Movie = Movie.objects.get(id=pk)
        except Movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    def put(self, request: Request, pk: str) -> Response:
        try:
            movie: Movie = Movie.objects.get(id=pk)
        except Movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, pk: str) -> Response:
        try:
            movie: Movie = Movie.objects.get(id=pk)
        except Movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ReviewsByMovieListView(APIView):

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        elif self.request.method == "POST":
            return [IsAuthenticated()]

        return super().get_permissions()

    def get(self, request: Request, pk: str) -> Response:
        try:
            movie: Movie = Movie.objects.get(id=pk)
        except Movie.DoesNotExist:
            raise NotFound("Genre not found")

        movies: BaseManager[Review] = movie.reviews.all()
        paginator = LimitOffsetPagination()
        paginated_movies: Optional[list[Movie]] = paginator.paginate_queryset(
            movies, request
        )
        serializer = ReviewSerializer(paginated_movies, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request: Request, pk: str) -> Response:
        try:
            movie: Movie = Movie.objects.get(id=pk)
        except Movie.DoesNotExist:
            raise NotFound("Genre not found")
        review_data = dict(request.data)
        review_data["user"] = request.user.pk
        review_data["movie"] = movie.id

        serializer = ReviewSerializer(data=review_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReviewByMovieDetailView(APIView):

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        elif self.request.method == "PUT":
            return [IsAuthenticated()]
        elif self.request.method == "DELETE":
            return [IsAuthenticated()]

        return super().get_permissions()

    def get(self, request: Request, movie_pk: str, review_pk: str) -> Response:
        try:
            movie: Movie = Movie.objects.get(id=movie_pk)
        except Movie.DoesNotExist:
            return Response("Movie id not Found", status=status.HTTP_404_NOT_FOUND)

        try:
            review = movie.reviews.get(id=review_pk)
        except Review.DoesNotExist:
            return Response("Review id not Found", status=status.HTTP_404_NOT_FOUND)

        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    def put(self, request: Request, movie_pk: str, review_pk: str) -> Response:
        try:
            movie: Movie = Movie.objects.get(id=movie_pk)
        except Movie.DoesNotExist:
            return Response("Movie id not Found", status=status.HTTP_404_NOT_FOUND)

        try:
            review: Review = movie.reviews.get(id=review_pk)
        except Review.DoesNotExist:
            return Response("Review id not Found", status=status.HTTP_404_NOT_FOUND)

        if review.user != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)

        review_data = dict(request.data)
        review_data["user"] = request.user.pk
        review_data["movie"] = movie.id

        serializer = ReviewSerializer(review, data=review_data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, movie_pk: str, review_pk: str) -> Response:
        try:
            movie: Movie = Movie.objects.get(id=movie_pk)
        except Movie.DoesNotExist:
            return Response("Movie id not Found", status=status.HTTP_404_NOT_FOUND)

        try:
            review = movie.reviews.get(id=review_pk)
        except Review.DoesNotExist:
            return Response("Review id not Found", status=status.HTTP_404_NOT_FOUND)

        if review.user != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)

        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
