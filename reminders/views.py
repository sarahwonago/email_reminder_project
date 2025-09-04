from rest_framework import generics
from .models import Reminder
from .serializers import ReminderSerializer
from .tasks import send_reminder


class ReminderListCreateView(generics.ListCreateAPIView):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer

    def perform_create(self, serializer):
        reminder = serializer.save()
        # schedule task exactly at scheduled_time
        send_reminder.apply_async((reminder.id,), eta=reminder.scheduled_time)


class ReminderDetailView(generics.RetrieveAPIView):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer
