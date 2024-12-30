from django.contrib import admin
from message_app.models import MessageBoard, Message

# Register your models here.

admin.site.register((MessageBoard, Message))