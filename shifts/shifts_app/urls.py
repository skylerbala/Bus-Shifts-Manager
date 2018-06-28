from django.conf.urls import include, url
from . import views

urlpatterns = [
    url('^$', views.HomeView.as_view(), name='index'),
    url('^shifts/$', views.shifts, name='shifts'),
    url('^shifts/add$', views.ShiftCreate.as_view(), name='shift-add'),
]
