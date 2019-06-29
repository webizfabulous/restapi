from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Api
from rest_framework.response import Response

from .serializers import ApiSerializer

@api_view(['GET'])
def api_list(request):
    if request.method== 'GET':
        obj = Api.objects.all()
        serializer = ApiSerializer(obj , many=True)
        return Response(serializer.data)

    