# from django.shortcuts import render
# from rest_framework import generics

from rest_framework.views import APIView
from signup_API.models import Application_Users
from API.serializers import*
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework import status


class Application_Users_View(APIView):
    # post api method for user signup 
    def post(self,request):
        
        data = request.data
          
        # took the field out from the reuest that sent
        Phone_number = data['Phone_number']
        Email = data['Email']


        # USER with same mobile number exists or not
        isPhoneNumber_Exist = Application_Users.objects.filter(Phone_number = Phone_number,).exists()
        # USER with same email exists or not
        isEmail_Exist = Application_Users.objects.filter(Email=Email, ).exists()
        user = Application_Users.objects.filter(Phone_number = Phone_number ,Email=Email, ).first()

        
        
        serializer = Application_Users_Serializers(data=request.data)
        
# if there is any problem is the serialisation or user existance 
        if serializer.is_valid():
          if isPhoneNumber_Exist :
            return Response(
                 {
                      'status' : status.HTTP_400_BAD_REQUEST,
                      'message' : "Mobile Number already exist",
                 }
            )
        
          if isEmail_Exist :
            return Response(
                 {
                      'status' : status.HTTP_400_BAD_REQUEST,
                      'message' : "Email already exist",
                 }
                 
             )
          serializer.save()
          return Response(
                    {
                      'status' : status.HTTP_201_CREATED,
                       'data'  :user,
                      'message' : "User Created Successfully",
                 }
                )
        else :
                return Response(
                    {
                      'status' : status.HTTP_400_BAD_REQUEST,
                      'message' : "SOMETHING WENT WRONG",
                 }
                )
        

# how to create simple api view with using the generics and mixins 


# class Application_Users_Details(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Application_Users.objects.all()
#     serializer_class = Application_Users_Serializers
#     lookup_field= 'pk'