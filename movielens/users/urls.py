from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login/$',views.user_login, name='user_login'),
    url(r'^logout/$', views.user_login, name='logout'),
    # url(r'^', include('django.contrib.auth.urls'))
    ]
