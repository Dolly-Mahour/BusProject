from django.shortcuts import render
from rest_framework.views import APIView
from Search_Places_API.models import search_bus_trips
from API.serializers import*
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework import status
from Search_Places_API.models import search_bus_trips
from Search_Places_API.models import search_bus_trips
# Create your views here.


class Search_Places_view(APIView):
    def post(self,request):
        data=request.data
        from_place = data['from_place_id']
        to_place = data['to_place_id']
        date = data['date']
        serializer = Search_Places_Serializers(data=request.data)
        result = search_bus_trips.objects.filter(to_place_id = to_place,from_place_id = from_place, on_date = date).exists()
        if serializer.is_valid():
            if result :
                result = search_bus_trips.objects.filter(to_place_id = to_place,from_place_id = from_place, on_date = date).values()
                return Response(
                    {
                        'status' : status.HTTP_200_OK,
                        'data' : result,
                        'message' : "Data match found Succesfully",
                    }
                )
            else:
                return Response(
                    {
                      'status' : status.HTTP_404_NOT_FOUND,
                      'message' : "No entry found",
                 })
        else:
            return Response(
                    {
                      'status' : status.HTTP_404_NOT_FOUND,
                      'message' : "serializer is not valid",
                 })

