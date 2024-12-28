from django.urls import path
from home_app.views import *

urlpatterns = [
    path('', home_view, name="home"),  
]
