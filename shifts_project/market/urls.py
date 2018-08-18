from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.market, name='index'),
    url(r'^cover/(?P<pk>[0-9]+)/$', views.market_cover, name='cover'),
]