from django.shortcuts import render
from django.http import HttpResponse
from .models import Rater, Rating, Movie

# Create your views here.
def all_movies(request):
    movies = Movie.objects.all()
    return render(request,
            'review/rater.html',
            {'movies': movies})

def rater_detail(request):
    raters = Rater.objects.all()
    return render(request,
                    'review/rater_detail.html',
                    {'raters':raters})


def all_raters(request):
    raters = Rater.objects.all()
    return render(request)
