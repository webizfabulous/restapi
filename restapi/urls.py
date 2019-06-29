
from django.contrib import admin
from django.urls import path

from apiapp.views import api_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/' , api_list),
]
