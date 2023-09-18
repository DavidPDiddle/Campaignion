from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Campaign, Quest, Session
from .serializers import CampaignSerializer, QuestSerializer, SessionSerializer

# Create your views here.

class CampaignView(generics.CreateAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer

class QuestView(generics.CreateAPIView):
    queryset = Quest.objects.all()
    serializer_class = CampaignSerializer

class SessionView(generics.CreateAPIView):
    queryset = Session.objects.all()
    serializer_class = CampaignSerializer