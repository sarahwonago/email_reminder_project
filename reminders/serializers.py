from rest_framework import serializers
from django.utils import timezone
from .models import Reminder


class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = "__all__"
        read_only_fields = ("sent", "created_at")

    def validate_scheduled_time(self, value):
        # must be timezone-aware and in the future
        if timezone.is_naive(value):
            raise serializers.ValidationError(
                "scheduled_time must be timezone-aware (include 'Z' or offset)."
            )
        if value <= timezone.now():
            raise serializers.ValidationError("scheduled_time must be in the future.")
        return value
