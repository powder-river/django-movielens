from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=300)

    def __str__(self):
        return self.title
class Rater(models.Model):
    age = models.IntegerField()
    gender = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=5)
    occupation = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id)



class Rating(models.Model):
    rating = models.IntegerField()
    movie = models.ForeignKey(Movie)
    rater = models.ForeignKey(Rater)


def load_ml_data():
    import csv
    import json
    import re

    users = []
    with open('ml-1m/users.dat') as f:
        reader = csv.DictReader([line.replace('::', '\t') for line in f],
                                fieldnames='UserID::Gender::Age::Occupation::Zip-code'.split('::'),
                                delimiter='\t')
        for row in reader:
            user = {
                'fields': {
                    'age': row['Age'],
                    'gender': row['Gender'],

                    'occupation': row['Occupation'],
                    'zipcode': row['Zip-code'],
                },
                'model': 'review.Rater',
                'pk': int(row['UserID']),
            }
        users.append(user)


    with open('users.json', 'w') as f:
        f.write(json.dumps(users))
