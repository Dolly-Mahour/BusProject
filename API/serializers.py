from rest_framework import serializers
from signup_API.models import Application_Users
from cities_API.models import place
from login_API.models import Login_Users
from Search_Places_API.models import search_bus_trips

class Application_Users_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Application_Users
        fields = "__all__"

class Places_Serializers(serializers.ModelSerializer):
    class Meta:
        model = place
        fields = "__all__"


class Login_Users_Serializers(serializers.Serializer):
    class Meta:
        model = Login_Users
        fields = "__all__"



class Search_Places_Serializers(serializers.ModelSerializer):
    class Meta:
        model = search_bus_trips
        fields = "__all__"

