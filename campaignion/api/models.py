from django.db import models

# Create your models here.
class Campaign(models.Model):
    name = models.TextField(unique=True)
    description = models.TextField()
    is_active = models.BooleanField(null=False, default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Quest(models.Model):
    name = models.TextField(unique=True)
    description = models.TextField()
    status = models.TextField()
    is_active = models.BooleanField(null=False, default=True)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class QuestNote(models.Model):
    description = models.TextField()
    quest = models.ForeignKey(Quest, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Session(models.Model):
    name = models.TextField(unique=True)
    description = models.TextField()
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    quest_notes = models.ForeignKey(QuestNote, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)