from django.db import models


class Reminder(models.Model):
    email = models.EmailField()
    message = models.TextField()
    scheduled_time = models.DateTimeField(
        help_text="Timezone-aware datetime (ISO 8601)"
    )
    sent = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Reminder to {self.email} at {self.scheduled_time}"
