from django.db import models
from django.contrib.auth.models import User, auth

# Create your models here.

class message(models.Model):
    user = models.ForeignKey(User, related_name='messages',  on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='message')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-modified_at',)

class ConversationMessage(models.Model):
    conversation = models.ForeignKey(message, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='created_messages', on_delete=models.CASCADE)