from django.conf.urls import url
from django.contrib import admin

# Register your models here.

urlpatterns = [
  url(r'^admin/', admin.site.urls),
]