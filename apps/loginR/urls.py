from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name="landing"),
    url(r'^register$', views.register, name="register"),
    url(r'^login$', views.login, name="login"),
    url(r'^logout$', views.logout, name="logout"),
    url(r'^friends$', views.success, name="dashboard"),
    url(r'^friends/(?P<id>\d+)$', views.friend, name="profile"),
    url(r'^add/(?P<id>\d+)$', views.add, name="add_friend"),
    url(r'^remove/(?P<id>\d+)$', views.remove, name="remove_friend"),
    ]
