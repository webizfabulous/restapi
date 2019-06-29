
from django.contrib import admin
from django.urls import path ,include
from .router import router

#from apiapp.views import api_list , api_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('api/' , api_list),
    #path('api/<int:index_id>/' , api_detail),
    path('apiapp/' , include('apiapp.urls' , namespace='restapi')),
    path('api/' , include(router.urls)), #including router.urls
]


