from rest_framework import serializers
from movie_app.models import Director, Movie, Review
from rest_framework.exceptions import ValidationError


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'text', 'movie', 'stars')


class MovieSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'duration', 'director', 'reviews', 'rating')

    def get_rating(self, movie):
        stars_list = [review.stars for review in movie.reviews.all()]
        return sum(stars_list) / len(stars_list)


class DirectorSerializer(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = ('id', 'name', 'movies_count')

    def get_movies_count(self, director):
        return director.movies.count()


class MovieValidateSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=3, max_length=100)
    description = serializers.CharField(default='No description')
    duration = serializers.FloatField()
    director_id = serializers.IntegerField()

    def validate_director_id(self, director_id):
        try:
            Director.objects.get(id=director_id)
        except Director.DoesNotExist:
            raise ValidationError('Director not found!')
        return director_id


class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField(min_length=3)
    movie_id = serializers.IntegerField()
    stars = serializers.IntegerField()

    def validate_movie_id(self, movie_id):
        try:
            Movie.objects.get(id=movie_id)
        except Movie.DoesNotExist:
            raise ValidationError('Movie is not found')
        return movie_id


class DirectorValidateSerializer(serializers.Serializer):
    name = serializers.CharField(min_length=3)
