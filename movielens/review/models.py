from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=300)


class Rater(models.Model):
    age = models.IntegerField()
    # rating = models.DecimalField()
    # movie = models.ForeignKey(Movie)


class Rating(models.Model):
    rating = models.IntegerField()
    movie = models.ForeignKey(Movie)
    rater = models.ForeignKey(Rater)
