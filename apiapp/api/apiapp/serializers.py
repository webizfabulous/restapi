from rest_framework import serializers
from apiapp.models import Api

class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Api
        fields = ['name','size','author','created']
        

