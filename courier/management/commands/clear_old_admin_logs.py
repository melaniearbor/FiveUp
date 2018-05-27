from django.core.management.base import BaseCommand
from django.contrib.admin.models import LogEntry


def clear_old_admin_logs():
    logs = LogEntry.objects.all()

    for i in range(2000, len(logs)):
        logs[i].delete()


class Command(BaseCommand):
    def handle(self, *args, **options):
        clear_old_admin_logs()
