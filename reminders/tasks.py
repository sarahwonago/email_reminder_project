from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone
from .models import Reminder


@shared_task(bind=True, max_retries=3, default_retry_delay=30)
def send_reminder(self, reminder_id: int):
    reminder = Reminder.objects.filter(id=reminder_id).first()
    if not reminder:
        return "not found"

    # only send once, at/after scheduled_time
    if reminder.sent:
        return "already sent"

    if reminder.scheduled_time > timezone.now():
        # Not time yet — requeue shortly (safety, though we schedule with ETA)
        raise self.retry(countdown=15)

    send_mail(
        subject="Your Reminder",
        message=reminder.message,
        from_email=None,  # uses DEFAULT_FROM_EMAIL
        recipient_list=[reminder.email],
        fail_silently=False,
    )
    reminder.sent = True
    reminder.save(update_fields=["sent"])
    return "sent"
