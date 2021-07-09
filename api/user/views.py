import json
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view

from .serializers import UserSerializer
from .models import User
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import random

@api_view(["POST",])
@csrf_exempt    
def userlogin(request):
    if not request.method == 'POST':
        return JsonResponse({ "error": "not a post request"})
    if request.method == "POST":
        print(request.POST)
        username =  request.POST['email']
        password =  request.POST['password']
        print(username, password)

        UserModel = User
        print(UserModel.objects.get(email=username))
        try:
            user = UserModel.objects.get(email=username)
            if user.password == password:  
                usr_dict = UserModel.objects.filter(
                email=username).values().first()
                usr_dict.pop("password")
                return JsonResponse({"user": usr_dict})   
                
        except UserModel.DoesNotExist:
            return JsonResponse({ "error": "Invalid email"})

    return JsonResponse({"error":"no user"})


# # create a viewset
class UserViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = User.objects.all()
    # specify serializer to be used
    serializer_class = UserSerializer

