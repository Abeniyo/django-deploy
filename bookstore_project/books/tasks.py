from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_notification_email(book_title):
    send_mail(
        subject='New Book Added',
        message=f'A new book "{book_title}" was added to the bookstore.',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[settings.EMAIL_HOST_USER],
        fail_silently=False,
    )
