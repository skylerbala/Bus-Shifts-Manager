from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.get_shifts, name='index'),
    url(r'^add/$', views.add_shift, name='add'),
    url(r'^update/(?P<pk>[0-9]+)/$', views.update_shift, name='update'),
    url(r'^delete/(?P<pk>[0-9]+)/$', views.delete_shift, name='delete'),
    url(r'^forbidden/$', views.forbidden, name='forbidden'),
]