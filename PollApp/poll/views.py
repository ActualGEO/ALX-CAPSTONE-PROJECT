from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Choice, Question, Vote
from . serializers import QuestionSerializer, ChoiceSerializer, VoteSerializer
# Create your views here.


class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class ChoiceViewSet(ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

class VoteViewSet(ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer