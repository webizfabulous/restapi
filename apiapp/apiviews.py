from  .models import Api
from .serializers import ApiSerializer
from rest_framework import viewsets


class ApiViewset(viewsets.ModelViewSet):
    #list , create ,  retrieve , update , partial update , destroy

    queryset = Api.objects.all()
    serializer_class = ApiSerializer

