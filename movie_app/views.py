from rest_framework.decorators import api_view
from movie_app.models import Director, Movie, Review
from rest_framework import status
from rest_framework.response import Response
from movie_app.serializer import DirectorSerializer, MovieSerializer, ReviewSerializer, MovieValidateSerializer, \
    ReviewValidateSerializer, DirectorValidateSerializer


# Create your views here.

@api_view(['GET', 'POST'])
def directors_view(request):
    if request.method == 'GET':
        directors = Director.objects.all()

        serializer = DirectorSerializer(directors, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = DirectorValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        name = serializer.validated_data.get('name')
        director = Director.objects.create(name=name)
        director.save()
        return Response(data={'message': "data received!"})


@api_view(['GET', 'PUT', 'DELETE'])
def directors_detail_view(request, **kwargs):
    try:
        director = Director.objects.get(id=kwargs['id'])
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Director not found!'})
    if request.method == 'GET':

        serializer = DirectorSerializer(director, many=False)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        serializer = DirectorValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        director.name = serializer.validated_data.get('name')
        director.save()
        return Response(data={'message': "data received!"})


@api_view(['GET', 'POST'])
def movie_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()

        serializer = MovieSerializer(movies, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = MovieValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        title = serializer.validated_data.get('title')
        description = serializer.validated_data.get('description')
        duration = serializer.validated_data.get('duration')
        director_id = serializer.validated_data.get('director_id')
        movie = Movie.objects.create(title=title, description=description, duration=duration, director_id=director_id)
        movie.save()
        return Response(data={'message': "data received!"})


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail_view(request, **kwargs):
    try:
        movie = Movie.objects.get(id=kwargs['id'])
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Movie not found!'})
    if request.method == 'GET':

        serializer = MovieSerializer(movie, many=False)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        serializer = MovieValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        movie.title = serializer.validated_data.get('title')
        movie.description = serializer.validated_data.get('description')
        movie.duration = serializer.validated_data.get('duration')
        movie.director_id = serializer.validated_data.get('director_id')
        movie.save()
        return Response(data={'message': "data received!"})


@api_view(['GET', 'POST'])
def review_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()

        serializer = ReviewSerializer(reviews, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = ReviewValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        text = serializer.validated_data.get('text')
        movie_id = serializer.validated_data.get('movie_id')
        stars = serializer.validated_data.get('stars')
        review = Review.objects.create(text=text, movie_id=movie_id, stars=stars)
        review.save()
        return Response(data={'message': "data received!"})


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_view(request, **kwargs):
    try:
        review = Review.objects.get(id=kwargs['id'])
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Review not found!'})

    if request.method == 'GET':

        serializer = ReviewSerializer(review, many=False)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        serializer = ReviewValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        review.text = serializer.validated_data.get('text')
        review.movie_id = serializer.validated_data.get('movie_id')
        review.stars = serializer.validated_data.get('stars')
        review.save()
        return Response(data={'message': "data received!"})
