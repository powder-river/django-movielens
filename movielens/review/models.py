from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=300)

    def __str__(self):
        return self.title
class Rater(models.Model):
    age = models.IntegerField()

    def __str__(self):
        return str(self.id)



class Rating(models.Model):
    rating = models.IntegerField()
    movie = models.ForeignKey(Movie)
    rater = models.ForeignKey(Rater)
