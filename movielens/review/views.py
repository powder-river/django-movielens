from django.shortcuts import render
from django.http import HttpResponse
from .models import Rater, Rating, Movie

# Create your views here.
def all_raters(request):
    raters = Rater.objects.all()
    status_strings = [str(r) for r in raters]
    # return HttpResponse('<br>'.join(status_strings))
    return render(request,
                  'review/rater.html')
                #   {'statuses': status_strings})

# def show_raters(request,rater_id):
#     Rater.objects.get(pk=rater_id)
#
#     return render(request,
#                  'review/rater.html',
