from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=300)
    genre = models.CharField(max_length=300)

    def average_rating(self):
        return self.rating_set.aggregate(models.Avg('rating'))['rating__avg']

    def __str__(self):
        return "{} {}".format(self.title, self.genre)
class Rater(models.Model):
    age = models.IntegerField()
    gender = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=5)
    occupation = models.CharField(max_length=100)

    def __str__(self):
        return "{} {} {} {}".format(self.age,self.gender,self.zipcode,self.occupation)



class Rating(models.Model):

    rater_id = models.ForeignKey(Rater)
    movie_id = models.ForeignKey(Movie)
    rating = models.IntegerField()



def load_rater_data():
    import csv
    import json
    import re

    users = []
    count = 1
    ratings = []
    with open('ml-1m/users.dat') as f:
        reader = csv.DictReader([line.replace('::', '\t') for line in f],
                                fieldnames='UserID::Gender::Age::Occupation::Zip-code'.split('::'),
                                delimiter='\t')
        for row in reader:
            print('Reading Row {}'.format(count))
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
            count +=1

    with open('users.json', 'w') as f:
        f.write(json.dumps(users))

def load_movie_data():
    movies = []
    count = 1
    import csv
    import re
    import json

    with open('ml-1m/movies.dat',encoding='ISO-8859-1') as f:
        reader = csv.DictReader([line.replace('::', '\t') for line in f],
                                fieldnames='MovieID::Title::Genre'.split('::'),
                                delimiter='\t')

        for row in reader:
            print('Reading Row {}'.format(count))
            movie = {
                'fields':{
                    'title': row['Title'],
                    'genre': row['Genre'],
                },
                'model': 'review.Movie',
                'pk':int(row['MovieID'])
            }
            movies.append(movie)
            count += 1
        print('Done Reading, Beginning Write')

    with open('movies.json', 'w') as f:
        f.write(json.dumps(movies))
    print('Done Writing')

def load_rating_data():
    ratings = []
    count = 1
    import csv
    import re
    import json

    with open('ml-1m/ratings.dat') as f:
        reader = csv.DictReader([line.replace('::', '\t') for line in f],
                                fieldnames='UserID::MovieID::Rating'.split('::'),
                                delimiter='\t')

        for row in reader:
            print('Reading Row {}'.format(count))
            rating = {
                'fields':{
                    'rater_id': row['UserID'],
                    'movie_id': row['MovieID'],
                    'rating': row['Rating']
                },
                'model': 'review.Rating',


            }
            ratings.append(rating)
            count += 1
        print('Done Reading, Beginning Write')

    with open('ratings.json', 'w') as f:
        f.write(json.dumps(ratings))
    print('Done Writing')
