from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Choice, Question, Vote
from . serializers import QuestionSerializer, ChoiceSerializer, VoteSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
# Create your views here.


class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    Authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    

class ChoiceViewSet(ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]



class VoteViewSet(ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
