from courier.management.commands.clear_old_send_times import clear_old_send_times
from django.test import TestCase
from courier.models import UserSendTime
from django.core.management import call_command
from fuauth.models import User


class TestClearOldSendTimes(TestCase):
    """Test the clear_old_send_times management command"""

    def setUp(self):
        test_user = User.objects.create(email="bland@house.com")

        for i in range(3000):
            UserSendTime.objects.create(user_id=test_user.pk)

    def test_old_send_times_are_deleted(self):
        """
        The number of UserSendTime entries should be 2000 after the clear_old_send_times
        is run.
        """
        num_logs = UserSendTime.objects.all().count()
        clear_old_send_times()
        new_num_logs = UserSendTime.objects.all().count()
        assert new_num_logs == 2000
        assert new_num_logs < num_logs

    def test_command_handle_calls_function(self):
        """
        The number of UserSendTime objects should be 2000 after the
        management command is called.
        """
        call_command("clear_old_send_times")
        assert UserSendTime.objects.all().count() == 2000
