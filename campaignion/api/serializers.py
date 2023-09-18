from rest_framework import serializers
from .models import Campaign, Quest, QuestNote, Session

class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = ('id', 'name', 'description', 'is_active', 'created_at', 'updated_at')

class QuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quest
        fields = ('id', 'name', 'description', 'status', 'is_active', 'created_at', 'updated_at')

class QuestNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestNote
        fields = ('id', 'description', 'created_at', 'updated_at')

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ('id', 'name', 'description', 'created_at', 'updated_at')