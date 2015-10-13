from django.shortcuts import render
from django.db.models import Avg, Count
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Rater, Rating, Movie

# Create your views here.
def all_movies(request):
    movies = Movie.objects.all()
    return render(request,
            'review/movies.html',
            {'movies': movies})


def rater_detail(request):
    raters = Rater.objects.all()
    return render(request,
                    'review/rater_detail.html',
                    {'raters':raters})

def show_rater(request, rater_id):
    rater = Rater.objects.get(pk=rater_id)
    ratings = Rating.objects.filter(rater_id=rater.id)
    return render(request,
                  'review/rater_ratings.html',
                  {'ratings': ratings,
                    'rater': rater,
                  })


def top_movies(request):
    popular_movies = Movie.objects.annotate(num_ratings=Count('rating')) \
                                  .filter(num_ratings__gte=50)

    movies = popular_movies.annotate(Avg('rating__rating')) \
                           .order_by('-rating__rating__avg')[:20]

    return render(request,
                  'review/top_movies.html',
                  {'movies': movies})

def profile_info(request, user_id):
    movie_user = User.objects.get(pk=user_id)
    return render(request, 'review/profile.html',
                            {'movie_user': movie_user})
