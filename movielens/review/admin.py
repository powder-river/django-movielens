from django.contrib import admin
from .models import Movie, Rater, Rating

class MovieAdmin(admin.ModelAdmin):
    list_display = ['id','title','genre']


class RaterAdmin(admin.ModelAdmin):
    list_dispay = ['id','age','gender','zipcode','occupation']



class RatingAdmin(admin.ModelAdmin):
    list_display =['rater_id','movie_id','rating']

# Register your models here.


admin.site.register(Movie,MovieAdmin)
admin.site.register(Rater,RaterAdmin)
admin.site.register(Rating,RatingAdmin)
