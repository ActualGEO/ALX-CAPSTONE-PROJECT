from .views import index, login_user, RegisterView
from django.urls import path

urlpatterns = [
    path('', index),
    path('login/', login_user),
    path('register/', RegisterView.as_view(), name='register'),
]