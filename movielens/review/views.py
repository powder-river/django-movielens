from django.shortcuts import render
from django.http import HttpResponse
from .models import Rater, Rating, Movie

# Create your views here.
def all_movies(request):
    movies = Movie.objects.all()
    return render(request,
            'review/rater.html',
            {'movies': movies})

def movie_detail(request,movie_id):
    movies = Movie.objects.all()
    return render(request,
                    'review/movie_detail.html',
                    {'movies':movies}
    )
