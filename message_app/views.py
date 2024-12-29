from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from message_app.forms import MessageForm
from message_app.models import MessageBoard


# Create your views here.

@login_required
def message_view(request):
    messageboard = get_object_or_404(MessageBoard, id=1)
    form = MessageForm()

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid:
            message = form.save(commit=False)
            message.author = request.user
            message.messageboard = messageboard
            message.save()

        else:
            messages.warning(request, 'Subscribe first')

        return redirect('messageboard')

    context = {'messageboard': messageboard, 'form': form}
    return render(request, 'a_message/index.html', context)


@login_required
def subscribe(request):
    messageboard = get_object_or_404(MessageBoard, id=1)

    if request.user not in messageboard.subscriber.all():
        messageboard.subscriber.add(request.user)
    else:
        messageboard.subscriber.remove(request.user)

    return redirect('messageboard')
