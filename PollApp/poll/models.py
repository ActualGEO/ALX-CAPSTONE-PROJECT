from django.db import models

# Create your models here.

from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    poll_question = models.CharField(max_length=300)
    publication_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.poll_question
    

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    poll_choice = models.CharField(max_length=100)


class Vote(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} voted {self.choice}"

