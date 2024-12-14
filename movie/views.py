from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from movie.models import Actor, Genre, Movie
from movie.serializers import ActorSerializer, GenreSerializer, MovieSerializer


class ActorListCreateView(APIView):
    def get(self, request: Request) -> Response:
        actors = Actor.objects.all()
        paginator = LimitOffsetPagination()
        paginated_actors = paginator.paginate_queryset(actors, request)
        serializer = ActorSerializer(paginated_actors, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request: Request) -> Response:
        serializer = ActorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ActorDetailView(APIView):
    def get(self, request: Request, pk: str) -> Response:
        try:
            actor = Actor.objects.get(id=pk)
        except Actor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ActorSerializer(actor)
        return Response(serializer.data)

    def put(self, request: Request, pk: str) -> Response:
        try:
            actor = Actor.objects.get(id=pk)
        except Actor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ActorSerializer(actor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, pk: str) -> Response:
        try:
            actor = Actor.objects.get(id=pk)
        except Actor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        actor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MoviesByActorListView(ListAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        actor_id = self.kwargs.get("pk")  # Retrieve actor_id from URL
        try:
            actor = Actor.objects.get(id=actor_id)
        except Actor.DoesNotExist:
            raise NotFound("Actor not found")
        return actor.movies.all()


class GenreListCreateView(APIView):

    def get(self, request: Request) -> Response:
        genre = Genre.objects.all()
        paginator = LimitOffsetPagination()
        paginated_actors = paginator.paginate_queryset(genre, request)
        serializer = GenreSerializer(paginated_actors, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request: Request) -> Response:
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GenreDetailView(APIView):
    def get(self, request: Request, pk: str) -> Response:
        try:
            genre = Genre.objects.get(id=pk)
        except Genre.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = GenreSerializer(genre)
        return Response(serializer.data)

    def put(self, request: Request, pk: str) -> Response:
        try:
            genre = Genre.objects.get(id=pk)
        except Genre.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = GenreSerializer(genre, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, pk: str) -> Response:
        try:
            genre = Genre.objects.get(id=pk)
        except Genre.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MoviesByGenreListView(ListAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        genre_id = self.kwargs.get("pk")
        try:
            genre = Genre.objects.get(id=genre_id)
        except Genre.DoesNotExist:
            raise NotFound("Genre not found")
        return genre.movies.all()


class MovieListCreateView(APIView):

    def get(self, request: Request) -> Response:
        movies = Movie.objects.all()
        paginator = LimitOffsetPagination()
        paginated_actors = paginator.paginate_queryset(movies, request)
        serializer = MovieSerializer(paginated_actors, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request: Request) -> Response:
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieDetailView(RetrieveUpdateDestroyAPIView):

    def get(self, request: Request, pk: str) -> Response:
        try:
            movie = Movie.objects.get(id=pk)
        except Movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    def put(self, request: Request, pk: str) -> Response:
        try:
            movie = Movie.objects.get(id=pk)
        except Movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, pk: str) -> Response:
        try:
            movie = Movie.objects.get(id=pk)
        except Movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
