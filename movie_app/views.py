from rest_framework.decorators import api_view
from movie_app.models import Director, Movie, Review
from rest_framework import status
from rest_framework.response import Response
from movie_app.serializer import DirectorSerializer, MovieSerializer, ReviewSerializer


# Create your views here.

@api_view(['GET'])
def directors_view(request):
    if request.method == 'GET':
        directors = Director.objects.all()

        serializer = DirectorSerializer(directors, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def directors_detail_view(request, **kwargs):
    if request.method == 'GET':
        try:
            director = Director.objects.get(id=kwargs['id'])
        except Director.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Director not found!'})

        serializer = DirectorSerializer(director, many=False)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def movie_view(request):
    if request.method == 'GET':
        directors = Movie.objects.all()

        serializer = MovieSerializer(directors, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def movie_detail_view(request, **kwargs):
    if request.method == 'GET':
        try:
            director = Movie.objects.get(id=kwargs['id'])
        except Movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Movie not found!'})

        serializer = MovieSerializer(director, many=False)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def review_view(request):
    if request.method == 'GET':
        directors = Review.objects.all()

        serializer = ReviewSerializer(directors, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def review_detail_view(request, **kwargs):
    if request.method == 'GET':
        try:
            director = Review.objects.get(id=kwargs['id'])
        except Review.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Review not found!'})

        serializer = ReviewSerializer(director, many=False)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def movies_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()

        serializer = ReviewSerializer(movies, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
