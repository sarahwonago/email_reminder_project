import os
from celery import Celery

# set default Django settings for Celery
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "email_reminder_project.settings")

app = Celery("email_reminder_project")

# Load task settings from Django settings with 'CELERY_' namespace
app.config_from_object("django.conf:settings", namespace="CELERY")

# Auto-discover tasks in all installed apps
app.autodiscover_tasks()
