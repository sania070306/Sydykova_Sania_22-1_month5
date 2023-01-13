from rest_framework.decorators import api_view
from movie_app.models import Director, Movie, Review
from rest_framework import status
from rest_framework.response import Response
from movie_app.serializer import DirectorSerializer, MovieSerializer, ReviewSerializer


# Create your views here.

@api_view(['GET', 'POST'])
def directors_view(request):
    if request.method == 'GET':
        directors = Director.objects.all()

        serializer = DirectorSerializer(directors, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        name = request.data.get('name')
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
        director.name = request.data.get('name')
        director.save()
        return Response(data={'message': "data received!"})


@api_view(['GET', 'POST'])
def movie_view(request):
    if request.method == 'GET':
        directors = Movie.objects.all()

        serializer = MovieSerializer(directors, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        title = request.data.get('title')
        description = request.data.get('description')
        duration = request.data.get('duration')
        director_id = request.data.get('director_id')
        movie = Movie.objects.create(title=title, description=description, duration=duration, director_id=director_id)
        movie.save()
        return Response(data={'message': "data received!"})


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail_view(request, **kwargs):
    try:
        director = Movie.objects.get(id=kwargs['id'])
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Movie not found!'})
    if request.method == 'GET':

        serializer = MovieSerializer(director, many=False)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        director.title = request.data.get('title')
        director.description = request.data.get('description')
        director.duration = request.data.get('duration')
        director.director_id = request.data.get('director_id')
        director.save()
        return Response(data={'message': "data received!"})


@api_view(['GET', 'POST'])
def review_view(request):
    if request.method == 'GET':
        directors = Review.objects.all()

        serializer = ReviewSerializer(directors, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        text = request.data.get('text')
        movie_id = request.data.get('movie_id')
        stars = request.data.get('stars')
        review = Review.objects.create(text=text, movie_id=movie_id, stars=stars)
        review.save()
        return Response(data={'message': "data received!"})


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_view(request, **kwargs):
    try:
        director = Review.objects.get(id=kwargs['id'])
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Review not found!'})

    if request.method == 'GET':

        serializer = ReviewSerializer(director, many=False)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        director.text = request.data.get('text')
        director.movie_id = request.data.get('movie_id')
        director.stars = request.data.get('stars')
        director.save()
        return Response(data={'message': "data received!"})
