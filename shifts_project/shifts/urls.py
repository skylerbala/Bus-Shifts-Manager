from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.get_shifts, name='index'),
    url(r'^add/$', views.add_shift, name='add'),
    url(r'^update/(?P<pk>[0-9]+)/$', views.update_shift, name='update'),
    url(r'^delete/(?P<pk>[0-9]+)/$', views.delete_shift, name='delete'),
    url(r'^coverage/$', views.coverage, name='coverage'),
    url(r'^coverage/(?P<pk>[0-9]+)/$', views.coverage_fill, name='coverage-fill'),
    url(r'^num-of-runs/', views.get_num_of_runs, name='num-of-runs'),
]
