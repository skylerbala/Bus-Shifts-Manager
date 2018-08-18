from django.conf.urls import url
from django.contrib.auth import views as authviews
from . import views

urlpatterns = [
  url(r'^$', views.login_redirect, name='login-redirect'),
  url(r'^login/$', authviews.login, {'template_name': 'accounts/login.html'}, name='login'),
  url(r'^logout/$', views.logout, name='logout'),
  url(r'^register/$', views.register, name='register'),
  url(r'^profile/$', views.profile, name='profile'),
  url(r'^update-profile/$', views.update_profile, name='update-profile'),
]
