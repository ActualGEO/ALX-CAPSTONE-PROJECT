from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username'
        ]


class RegisterSerializer(serializers.ModelSerializer):
     password = serializers.CharField(write_only=True)
     
     class Meta:
          model = User
          fields = ['username', 'email', 'password']


     def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']  # hashed automatically
        )
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'date_joined']
        read_only_fields = ['date_joined', 'username', 'email']





class LoginSerializer(serializers.Serializer):
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
          
          
            
        
          
               