from django.shortcuts import render
# from rest_framework.decorators import api_view
# from .models import Api
# from rest_framework.response import Response
# from rest_framework import status #importing status
# from .serializers import ApiSerializer



# #get for Get method
# #post for post method
# #adding methods
# @api_view(['GET' , "POST"])
# def api_list(request):
#     if request.method== 'GET':
#         obj = Api.objects.all()
#         serializer = ApiSerializer(obj , many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = ApiSerializer(data=request.data)
#         if serializer.is_valid(): #if serializer is valid
#             serializer.save() #save it
#             #return the saved value with response code 201
#             return Response(serializer.data , status=status.HTTP_201_CREATED)
#         #else if the serializer is not valid return request error with code 400
#         return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)



# #this is get
# #it helps to get data
# #put==update
# @api_view(['GET','PUT'])
# def api_detail(request , index_id):
#     try: #try
#         #if obj is available
#         obj = Api.objects.get(pk=index_id)
#     except Api.DoesNotExist: #if Api doesnot exist
#         return Response(status=status.HTTP_404_NOT_FOUND) #return 404 not found
#     if request.method == 'GET':
#         serializer = ApiSerializer(obj) #passing which we wanna serialize
#         return Response(serializer.data) #.data returns serialized data
#     elif request.method=='PUT': #if request is PUT
#         serializer = ApiSerializer(obj , data=request.data) #requesting data to update
#         if serializer.is_valid(): #if data is valid
#             serializer.save() #save the serializer
#             return Response(serializer.data) #return saved data
#         return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)


#just test function
def index(request):
    pass
    