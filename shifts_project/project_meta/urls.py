"""shifts_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^', include('accounts.urls', namespace='accounts')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/', include('home.urls', namespace='home')),
    url(r'^shifts/', include('shifts.urls', namespace='shifts')),
    url(r'^my-shifts/', include('my_shifts.urls', namespace='my-shifts')),
    url(r'^shift-groups/', include('shift_groups.urls', namespace='shift-groups')), 
    url(r'^market/', include('market.urls', namespace='market')),
    url(r'^employees/', include('employees.urls', namespace='employees')),
    url(r'^upload-excel/', include('uploadexcel.urls', namespace='upload-excel')), 
]
