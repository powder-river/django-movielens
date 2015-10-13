from django.conf.urls import url
from django.contrib.auth.models import User
from . import views

urlpatterns = [
    url(r'^movies/all', views.all_movies, name='movie_list'),
    url(r'^raters/all', views.rater_detail, name='rater_list'),
    url(r'^movies/top_movies', views.top_movies, name='best_movie'),
    url(r'^users/(?P<user_id>\d+)', views.profile_info, name='user_profile'),
    url(r'^raters/(?P<rater_id>\d+)$', views.show_rater, name='rater_detail')
]
