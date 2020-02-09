from courier.models import UserSendTime
from django.test import TestCase
from freezegun import freeze_time
from fuauth.models import User


class TestUserSendTime(TestCase):
    """
    Basic tests for the UserSendTime model.
    """

    @freeze_time("2019-12-28 12:31")
    def setUp(self):

        self.noof = User.objects.create_user(
            name="Noofie",
            phone_number="777-777-7777",
            carrier="ATT",
            password="password",
            user_timezone="HAWAII",
            email="noofie@emailzzz.com",
        )

        self.send_time = UserSendTime.objects.create(user=self.noof)

    def test_message_string_repr(self):
        """
        The message object should have a nice string representation.
        """
        assert str(self.send_time) == "noofie@emailzzz.com_2019-12-28 12:31:00+00:00"

    def deleting_a_user_deletes_user_messages(self):
        """
        If a user is deleted, all related messages should be deleted as well.
        """
        assert len(UserSendTime.objects.filter(user=self.noof)) == 1
        self.noof.delete()
        assert len(UserSendTime.objects.filter(user=self.noof)) == 0
