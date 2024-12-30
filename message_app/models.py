from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class MessageBoard(models.Model):
    subscriber = models.ManyToManyField(User, related_name='messageboard', blank=True)

    def __str__(self):
        return str(self.id)


class Message(models.Model):
    messageboard = models.ForeignKey(MessageBoard, on_delete=models.CASCADE, related_name='messages')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages')
    body = models.TextField(max_length=3000)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.author.username