from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username'
        ]

class LoginSerializer(serializers.ModelSerializer):
     username = serializers.CharField()
     password = serializers.CharField(write_only = True)

     def validate(self, data):
          
          username = data.get('username')
          password = data.get('password')

          if username and password:
               user = authenticate(username=username, password=password)

               if user is None:
                    raise serializers.ValidationError('Invalid Credentials')
               data['user'] = user

               return data
          else:
               raise serializers.ValidationError('Both username and password are required')
          
          
            
        
          
               