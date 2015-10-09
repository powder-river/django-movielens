from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^movies/all', views.all_movies, name='movie_list'),
    url(r'^raters/all', views.rater_detail, name='rater_list'),
    url(r'^raters/(?P<rater_id>\d+)$', views.show_rater, name='rater_detail')
    # url(r'movie/(?P<movie_id>\d+)$', views.movie_detail)
    # url(r'^statuses/', views.recent_statuses),
    # url(r'^user/(?P<user_id>\d+)$', views.show_user),
    # url(r'^user/(?P<username>\S+)$', views.show_user_by_username),
]
