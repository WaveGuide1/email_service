from django.urls import path

from message_app.views import *

urlpatterns = [
    path('', message_view, name='messageboard'),
    path('subscribe/', subscribe, name='subscribe'),
    path('newsletter/', newsletter, name='newsletter'),
]