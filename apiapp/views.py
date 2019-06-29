from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Api
from rest_framework.response import Response
from rest_framework import status #importing status
from .serializers import ApiSerializer

#adding methods
@api_view(['GET' , "POST"])
def api_list(request):
    if request.method== 'GET':
        obj = Api.objects.all()
        serializer = ApiSerializer(obj , many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ApiSerializer(data=request.data)
        if serializer.is_valid(): #if serializer is valid
            serializer.save() #save it
            #return the saved value with response code 201
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        #else if the serializer is not valid return request error with code 400
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)


