from  apiapp.models import Api
from .serializers import ApiSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class ApiViewset(viewsets.ModelViewSet):
    #list , create ,  retrieve , update , partial update , destroy

    queryset = Api.objects.all()
    serializer_class = ApiSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


    #method=get
    @action(methods=['get'] , detail=False) #detail=false means dont show this view on detail view
    def newest(self,request):
        newest = self.get_queryset().order_by('created').last() #gettting the last created model
        serializer = self.get_serializer_class()(newest) #setting that model to serializer or say serializing the newest data
        return Response(serializer.data) #returning jsonrespons
    