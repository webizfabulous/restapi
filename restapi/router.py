from apiapp.api.apiapp.apiviews import ApiViewset
from rest_framework import routers


router = routers.DefaultRouter()
router.register('restapis' , ApiViewset) #run ApiViewset when we go to /restapis url
#router accepts 3 values : one url name, 2nd viewsets and 3rd basE_name
#the url name provided here can be used with urls.py
# urls.py+router


