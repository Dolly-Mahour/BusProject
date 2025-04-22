from django.shortcuts import render
from rest_framework import generics
from API.serializers import Places_Serializers
from .models import place

# Create your views here.

class places_View(generics.ListAPIView):
    queryset = place.objects.all()
    serializer_class = Places_Serializers