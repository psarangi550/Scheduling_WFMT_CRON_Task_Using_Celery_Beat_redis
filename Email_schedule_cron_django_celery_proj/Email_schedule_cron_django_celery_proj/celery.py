from __future__ import absolute_import,unicode_literals
from datetime import timezone
from celery.schedules import crontab
from celery import Celery

import os

# from celery.app.defaults import Namespace

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Email_schedule_cron_django_celery_proj.settings")

app=Celery("Email_schedule_cron_django_celery_proj")

# app.conf.beat_schedule={
#     "schedule_task":{
#         "task":"Email_schedule_cron_django_celery_app.tasks.send_email",
#         "schedule":crontab(hour=14,minute=18),
#     }
# }

app.conf.enable_utc=False

app.conf.update(timezone="Asia/Kolkata")

app.config_from_object("django.conf:settings",namespace="CELERY")

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f" Request {self.request !r}")
    
    