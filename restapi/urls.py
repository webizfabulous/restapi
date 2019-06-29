
from django.contrib import admin
from django.urls import path ,include
from .router import router
from rest_framework.authtoken import views
#from apiapp.views import api_list , api_detail
from django.contrib.auth.views import LoginView



urlpatterns = [
    path('admin/', admin.site.urls),
    #path('api/' , api_list),
    #path('api/<int:index_id>/' , api_detail),
    path('apiapp/' , include('apiapp.urls' , namespace='restapi')),
    path('api/' , include(router.urls)), #including router.urls
    #views provided by rest_framework
    path('api-token-auth/' , views.obtain_auth_token  , name='api-token-auth'),
    path('login/' , LoginView.as_view() , name='login'),
]


