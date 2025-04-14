from django.shortcuts import render
from signup_API.models import Application_Users
from rest_framework import generics
from rest_framework.views import APIView
from API.serializers import*
# Create your views here.


class Application_Users_View(generics.ListCreateAPIView):
    queryset = Application_Users.objects.all()
    serializer_class = Application_Users_Serializers

class Application_Users_Details(generics.RetrieveUpdateDestroyAPIView):
    queryset = Application_Users.objects.all()
    serializer_class = Application_Users_Serializers
    lookup_field= 'pk'