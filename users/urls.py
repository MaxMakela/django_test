from django.urls import path
from .views import CreationUser

urlpatterns = [
    path('registration/', CreationUser.as_view(), name='registration'),
]
