from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login/$',views.user_login, name='user_login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    # url(r'^', include('django.contrib.auth.urls'))
    ]
