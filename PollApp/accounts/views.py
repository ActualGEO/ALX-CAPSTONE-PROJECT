from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import LoginSerializer, UserSerializer
from rest_framework.authtoken.models import Token
from rest_framework import status


@api_view(['GET'])
def index(request):

    return Response({"Welcom to api"})


@api_view(['POST'])
def login_user(request):
    serializer = LoginSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.validated_data['user']

        token, created = Token.objects.get_or_create(user=user)
        user_data = Userserializer(user).data

        return Response({
            'token': token.key,
            'user': user_data
        },   status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
