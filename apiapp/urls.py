from django.urls import path 
from .views import index

app_name = 'restapi'

urlpatterns = [
    path('' , index , name='index')
]
