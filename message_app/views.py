import threading
from email.message import EmailMessage

from django.contrib import messages
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from message_app.forms import MessageForm
from message_app.models import MessageBoard
from message_app.task import send_email_task


# Create your views here.

@login_required
def message_view(request):
    messageboard = get_object_or_404(MessageBoard, id=1)
    form = MessageForm()

    if request.method == 'POST':
        if request.user in messageboard.subscriber.all():

            form = MessageForm(request.POST)
            if form.is_valid():
                message = form.save(commit=False)
                message.author = request.user
                message.messageboard = messageboard
                message.save()
                send_email(message)

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


def send_email(message):
    messageboard = message.messageboard
    subscribers = messageboard.subscriber.all()

    for subscriber in subscribers:
        subject = f"Message from {message.author.profile.name}"
        body = f"{message.author.profile.name}: {message.body}\n\nRegards from \n Email Service"

        send_email_task.delay(subject, body, subscriber.email)

