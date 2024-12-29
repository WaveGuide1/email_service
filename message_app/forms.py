from django.forms import ModelForm
from django import forms
from message_app.models import *


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['body']
        widgets = {'body': forms.TextInput(attrs={'placeholder': 'write a message',
                                                  'class': 'p-4 text-black', 'maxlength': 3000})}