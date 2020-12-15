from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class AddUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User    #taghire username va password ham emkan pazire
        fields = ["username", "first_name","last_name","password","email"]

    def validate_password(self, data):
        print('password-----------------',data)
        data = make_password(data)
        return data

class UpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["password","username","first_name","last_name","email"]
    def validate(self, data):
        if self.context['Updating_password'] == True:
            data['password'] = make_password(data['password'])
        return data
        

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username","first_name","last_name","email"]