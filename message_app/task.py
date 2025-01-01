from datetime import datetime

from celery import shared_task
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from message_app.models import *


@shared_task(name='email_service_notification')
def send_email_task(subject, body, emailaddress):
    email = EmailMessage(subject, body, to=[emailaddress])
    email.send()
    return emailaddress


@shared_task(name='email_service_newsletter')
def send_newsletter():
    subject = "Email Service Monthly Newsletter"
    subscribers = MessageBoard.objects.get(id=1).subscriber.filter(
        profile__unsubscribe_newsletter=True
    )

    for subscriber in subscribers:
        body = render_to_string('a_message/newsletter.html', {'name': subscriber.profile.name})

        email = EmailMessage(subject, body, to=[subscriber.email])
        email.content_subtype = 'html'
        email.send()

    current_month = datetime.now().strftime('%B')
    count = subscribers.count()
    return f"In the month of {current_month}, newsletter was sent to {count} subscribers"

