from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . views import QuestionViewSet, ChoiceViewSet, VoteViewSet

router = DefaultRouter()
router.register(r'question', QuestionViewSet)
router.register(r'choice', ChoiceViewSet)
router.register(r'vote', VoteViewSet)

urlpatterns = [
    path('', include(router.urls))
]