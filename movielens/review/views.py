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

def show_rater(request, rater_id):
    rater = Rater.objects.get(pk=rater_id)
    ratings = Rating.objects.filter(rater_id=rater.id)
    return render(request,
                  'review/rater_ratings.html',
                  {'ratings': ratings,
                    'rater': rater,
                  })


# def show_user(request, user_id):
#     user = User.objects.get(pk=user_id)
#     statuses = user.status_set.all().order_by('-posted_at')
#
#     return render(request,
#                   'updates/user.html',
#                   {'user': user,
#                    'statuses': statuses})
