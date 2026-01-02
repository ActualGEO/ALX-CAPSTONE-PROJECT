from .views import index, login_user
from django.urls import path

urlpatterns = [
    path('', index),
    path('login/', login_user),
]