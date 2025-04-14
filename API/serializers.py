from rest_framework import serializers
from signup_API.models import Application_Users


class Application_Users_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Application_Users
        fields = "__all__"