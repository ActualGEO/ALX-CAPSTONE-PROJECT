from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import LoginSerializer, UserSerializer, RegisterSerializer
from rest_framework.authtoken.models import Token
from rest_framework import (
    status,
    generics,
    permissions,

)
from accounts.serializers import UserProfileSerializer
from django.contrib.auth import get_user_model


User = get_user_model()


@api_view(['GET'])
def index(request):

    return Response({"Welcom to api"})


@api_view(['POST'])
def login_user(request):
    serializer = LoginSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.validated_data['user']

        token, created = Token.objects.get_or_create(user=user)
        user_data = UserSerializer(user).data

        return Response({
            'token': token.key,
            'user': user_data
        },   status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegisterView(generics.CreateAPIView):
    """The logic here creates a user and returns a token
        that can be used in all authentication required views,
        by overriding the create method.
    """
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        autthentication_classes = []
        

        user = serializer.save()
        token, _ = Token.objects.get_or_create(user=user)

        return Response({
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,

            },
            "token": token.key
        })
