from django.shortcuts import render
# from login_API.models import Login_Users
from rest_framework import generics
from rest_framework.views import APIView
from API.serializers import*
from rest_framework.response import Response
from signup_API.models import Application_Users
from rest_framework.decorators import APIView
# Create your views here.

class Login_User_Views(APIView):
    def post(self,request):
        data = request.data
        print(data)
        phone = request.data['Phone_number']
        password = request.data['Password']
        # number = Application_Users.objects.filter(Phone_number_in = request.POST.get('Phone_number'))
        isExist = Application_Users.objects.filter(Phone_number = phone , Password = password).exists()
        object = Application_Users.objects.filter(Phone_number = phone , Password = password).first()
        if isExist:
            print(isExist)
            return Response({
                "status" : True,
                "data" : {
                    "Username": object.Username,
                    "User_or_Agent": object.User_or_Agent,
                    "Email": object.Email,
                    "Phone_number": object.Phone_number,
                    "Referral_code": object.Referral_code
                }  
             })
        else :
            return Response({
                "status" : False,
                "data" : "NO Data Found", 
             })
        
        


