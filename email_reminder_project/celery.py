import os
from email_reminder_project.celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "email_reminder_project.settings")

app = Celery("email_reminder_project")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
