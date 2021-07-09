from .models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from rest_framework.decorators import authentication_classes, permission_classes


    

class UserSerializer(serializers.ModelSerializer):
   
    # password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = User.objects.create(
            name=validated_data['name'],
            email=validated_data['email'],
            password=validated_data['password'],
        )

        return user
    
    

    class Meta:
        model = User
        fields = ('email',"name",'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    


