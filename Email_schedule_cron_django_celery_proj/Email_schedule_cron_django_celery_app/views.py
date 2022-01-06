from django.shortcuts import render,HttpResponse
from .tasks import send_email
from django.core.mail import send_mail
from django.conf import settings
from .forms import EmailForm
from django_celery_beat.models import PeriodicTask,CrontabSchedule
# Create your views here.

def index(request, *args, **kwargs):
    # send_email()
    send_email.delay()
    # email_subject = "wfmt email demo"
    # message = "This is a Test Email from WFMT using celery"
    # send_mail(
    #     email_subject,
    #     message,
    #     settings.DEFAULT_FROM_EMAIL,
    #     ["psarangi50@gmail.com",],
    #     fail_silently=False
    # )
    return HttpResponse("Email been Sent")


def email_temp(request, *args, **kwargs):
    if request.method == "POST":
        form=EmailForm(request.POST)
        if form.is_valid():
            hour=int(form.cleaned_data["hour"])
            minute=int(form.cleaned_data["minute"])
            cron_schedule,created=CrontabSchedule.objects.get_or_create(hour=hour,minute=minute)
            tsk=PeriodicTask.objects.create(name="schedule_email2",task=send_email,crontab=cron_schedule)
            tsk.save()
            return HttpResponse("Email Sent")
    form=EmailForm()
    return render(request,"Email_schedule_cron_django_celery_app/emailform.html",{"form":form})
