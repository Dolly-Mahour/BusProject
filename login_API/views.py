from django.shortcuts import render
# from login_API.models import Login_Users
from rest_framework import generics
from rest_framework.views import APIView
from API.serializers import*
from rest_framework.response import Response
from signup_API.models import Application_Users
from rest_framework.decorators import APIView
from django.contrib.auth import authenticate
from API.Token_Generate import get_tokens_for_user
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.

class Login_User_Views(APIView):
    def post(self,request):
      try :      
        data = request.data
        print(data)
        Phone_number = request.data['Phone_number']
        Password = request.data['Password']
        isExist = Application_Users.objects.filter(Phone_number = Phone_number , Password = Password).exists()
        if isExist:
            
            object = Application_Users.objects.filter(Phone_number = Phone_number , Password = Password).first()
            
            tokens = get_tokens_for_user(object)
            refresh = tokens["refresh"]
            access = tokens["access"]
            if object is None :
               return Response({
                    "status" : 400,
                    "message" : "enter valid information",
                    "data" :{}, 
                    
               })
            return Response({
                "status" : 200,
                "data" :"login",
                "message": "Login Successfully",
                "access" : access,
                "refresh" : refresh,
                "token" :tokens,
             })
        else :
            return Response({
                "status" : 400,
                "message" : "something went wrong",
                "data" : "NO Data Found", 
             })
      except Exception as e:
         print(e)
        
        


