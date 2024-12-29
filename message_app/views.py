from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.

@login_required
def message_view(request):
    return render(request, 'a_message/index.html')
