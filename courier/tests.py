from datetime import datetime

from django.test import TestCase
from fuauth.models import User

from .models import UserSendTime


class TestUserSendTimeModel(TestCase):
    def setUp(self):

        self.noof = User.objects.create_user(
            name="Noofie",
            phone_number="777-777-7777",
            carrier="ATT",
            password="password",
            user_timezone="HAWAII",
            email="noofie@emailzzz.com",
        )

        self.noof_time = UserSendTime(
            user=self.noof, scheduled_time=datetime(2019, 12, 28, 22, 6, 44)
        )

    def test_usersendtime_string_repr(self):

        assert str(self.noof_time) == "noofie@emailzzz.com_2019-12-28 22:06:44"
