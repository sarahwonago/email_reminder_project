from django.contrib import admin
from .models import Reminder


@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    list_display = ("email", "scheduled_time", "sent", "created_at")
    list_filter = ("sent",)
    search_fields = ("email", "message")
