from django.urls import path
from movie_app.views import (directors_view, directors_detail_view,
                             movie_view, movie_detail_view,
                             review_view, review_detail_view)

urlpatterns = [
    path('directors/', directors_view),
    path('directors/<int:id>/', directors_detail_view),
    path('movies/', movie_view),
    path('movies/<int:id>/', movie_detail_view),
    path('reviews/', review_view),
    path('reviews/<int:id>/', review_detail_view)
]
