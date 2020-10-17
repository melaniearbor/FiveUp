import uuid

from courier.management.commands.clear_old_admin_logs import \
    clear_old_admin_logs
from django.contrib.admin.models import LogEntry, ADDITION
from django.core.management import call_command
from django.test import TestCase

from fuauth.models import User


class TestClearOldAdminLogs(TestCase):
    """Test the clear_old_admin_logs management command"""

    def setUp(self):
        user = User.objects.create_user(
            name="Melanie",
            phone_number="777-777-7777",
            carrier="ATT",
            password="password",
            user_timezone="HAWAII",
            email="melanie@emailzzz.com",
        )
        for i in range(3000):
            LogEntry.objects.create(action_flag=ADDITION, user_id=user.id)

    def test_old_admin_logs_are_deleted(self):
        """
        The number of log entries should be 2000 after the clear_old_admin_logs
        is run.
        """
        num_logs = LogEntry.objects.all().count()
        clear_old_admin_logs()
        new_num_logs = LogEntry.objects.all().count()
        assert new_num_logs == 2000
        assert new_num_logs < num_logs

    def test_command_handle_calls_function(self):
        call_command("clear_old_admin_logs")
        assert LogEntry.objects.all().count() == 2000
