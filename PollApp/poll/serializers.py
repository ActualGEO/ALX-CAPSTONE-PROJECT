from .models import Question, User, Choice, Vote
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Question
        fields = '__all__'


class ChoiceSerializer(serializers.ModelSerializer):
    question = QuestionSerializer(read_only=True)
    class Meta:
        model = Choice
        fields = '__all__'


class VoteSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    question = QuestionSerializer(read_only=True)
    choice = ChoiceSerializer(read_only=True)
    class Meta:
        model = Vote
        fields = '__all__'