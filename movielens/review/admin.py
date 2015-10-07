from django.contrib import admin
from .models import Movie, Rater, Rating

class MovieAdmin(admin.ModelAdmin):
    list_display = ['id','title']


class RaterAdmin(admin.ModelAdmin):
    list_dispay = ['id','age']



class RatingAdmin(admin.ModelAdmin):
    list_display =['movie','rating','rater']

# Register your models here.


admin.site.register(Movie,MovieAdmin)
admin.site.register(Rater,RaterAdmin)
admin.site.register(Rating,RatingAdmin)
