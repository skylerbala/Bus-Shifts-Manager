from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.upload, name='uplink'),
    url(r'^import/', views.import_data, name="import"),
]