from rest_framework.views import APIView
from API.serializers import*
from rest_framework.response import Response
from signup_API.models import Application_Users
from rest_framework.decorators import APIView
from API.Token_Generate import get_tokens_for_user


# from rest_framework_simplejwt.tokens import RefreshToken
# from django.shortcuts import render
# from rest_framework import generics
# from django.contrib.auth import authenticate


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
            User_data = Application_Users.objects.filter(Phone_number = Phone_number , Password = Password).values()
            tokens = get_tokens_for_user(object)
            refresh = tokens["refresh"]
            access = tokens["access"]
            if object is None :
               return Response({
                    "status" : 401,
                    "message" : "Enter Valid Credentials",
                    
               })
            else:
                return Response({
                    "status" : 200,
                    "message": "Login Successfully",
                    "token" :tokens,
                    "User" :User_data,
                })
        else :
            return Response({
                "status" : 401,
                "message" : "Enter Valid Credentials",
             })
      except Exception as e:
         print("error from the api ",e)
        
        


