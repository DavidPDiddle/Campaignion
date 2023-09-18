from django.urls import path
from .views import index

urlpatterns = [
    path('campaign', index),
    path('quest', index),
    path('session', index)
]