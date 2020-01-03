from django.core.management.base import BaseCommand
from email_log.models import Email


def clear_old_email_logs():
    email_logs = Email.objects.all()

    for i in range(2000, len(email_logs)):
        email_logs[i].delete()


class Command(BaseCommand):
    def handle(self, *args, **options):
        clear_old_email_logs()
