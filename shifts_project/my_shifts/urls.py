from django.conf.urls import include, url
from . import views

urlpatterns = [
  url(r'^$', views.my_shifts, name='index'),
  url(r'^post/(?P<pk>[0-9]+)/$', views.my_shifts_post, name='post'),
]
