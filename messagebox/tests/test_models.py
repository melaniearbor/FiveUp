import datetime

from django.test import TestCase
from freezegun import freeze_time
from fuauth.models import User

from ..models import Message


class TestMessageBox(TestCase):
    """
    Basic tests for the message box.
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

        self.message = Message.objects.create(
            recipient=self.noof, message_text="You are beautiful", sender_name="Melanie"
        )

    def test_message_string_repr(self):
        """
        The message object should have a nice string representation.
        """
        assert str(self.message) == "Melanie_2019-12-28 12:31:00+00:00"
