from django.shortcuts import render
from signup_API.models import Application_Users
from rest_framework import generics
from rest_framework.views import APIView
from API.serializers import*
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework import status
# Create your views here.


class Application_Users_View(APIView):
    # queryset = Application_Users.objects.all()
    # serializer_class = Application_Users_Serializers
    def post(self,request):
        data = request.data
        print(data)
        Phone_number = request.data['Phone_number']
        Email = request.data['Email']
        isExist = Application_Users.objects.filter(Phone_number = Phone_number ,Email=Email, ).exists()
        isPhoneNumber_Exist = Application_Users.objects.filter(Phone_number = Phone_number,).exists()
        isEmail_Exist = Application_Users.objects.filter(Email=Email, ).exists()

        if isPhoneNumber_Exist :
            return Response(
                 {
                      'status' : status.HTTP_400_BAD_REQUEST,
                      'error' : "Phone_number",
                 }
            )
        if isEmail_Exist :
            print(isExist)
            return Response(
                 {
                      'status' : status.HTTP_400_BAD_REQUEST,
                      'problem' : "Email",
                 }
                 
             )
        
        serializer = Application_Users_Serializers(data=request.data)
        if serializer.is_valid() and isExist == False:
                serializer.save()
                return Response(
                    {
                      'status' : status.HTTP_201_CREATED,
                      'created' : "created",
                 }
                )
        else :
                return Response(
                    {
                      'status' : status.HTTP_400_BAD_REQUEST,
                      'problem' : "bad request",
                 }
                )
        
        
# class Application_Users_Details(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Application_Users.objects.all()
#     serializer_class = Application_Users_Serializers
#     lookup_field= 'pk'