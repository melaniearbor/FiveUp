from courier.management.commands.clear_old_email_logs import clear_old_email_logs
from email_log.models import Email
from django.test import TestCase
from django.core.management import call_command


class TestClearOldEmailLogs(TestCase):
    """Test the clear_old_email_logs management command"""

    def setUp(self):
        for i in range(3000):
            Email.objects.create()

    def test_old_email_logs_are_deleted(self):
        """
        The number of email entries should be 2000 after the clear_old_email_logs
        is run.
        """
        num_logs = Email.objects.all().count()
        clear_old_email_logs()
        new_num_logs = Email.objects.all().count()
        assert new_num_logs == 2000
        assert new_num_logs < num_logs

    def test_command_handle_calls_function(self):
        """
        The number of email objects should be 2000 after the
        management command is called.
        """
        call_command("clear_old_email_logs")
        assert Email.objects.all().count() == 2000
