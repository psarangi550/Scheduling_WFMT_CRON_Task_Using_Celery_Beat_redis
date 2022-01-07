from __future__ import absolute_import,unicode_literals
from django.core.mail import send_mail
from celery import shared_task
from django.conf import settings

# @shared_task
# def send_email():
#     email_subject = "wfmt email demo"
#     message = "This is a Test Email from WFMT using celery"
#     send_mail(
#         email_subject,
#         message,
#         settings.DEFAULT_FROM_EMAIL,
#         ["psarangi50@gmail.com",],
#         fail_silently=False
#     )
#     return "Done"

@shared_task
def add(a,b):
    result=a+b
    print(result)
    return result

    