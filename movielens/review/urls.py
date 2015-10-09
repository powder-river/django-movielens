from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^movies/all', views.all_movies, name='movie_list'),
    url(r'^raters/all', views.rater_detail, name='rater_list'),
    url(r'^raters/(?P<rater_id>\d+)$', views.show_rater, name='rater_detail')
]
