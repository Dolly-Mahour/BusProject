from rest_framework import serializers
from signup_API.models import Application_Users
from cities_API.models import place
from login_API.models import Login_Users

class Application_Users_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Application_Users
        fields = "__all__"

class Places_Serializers(serializers.ModelSerializer):
    class Meta:
        model = place
        fields = "__all__"


class Login_Users_Serializers(serializers.Serializer):
    # number = serializers.IntegerField()
    # password = serializers.CharField()
    class Meta:
        model = Login_Users
        fields = "__all__"

