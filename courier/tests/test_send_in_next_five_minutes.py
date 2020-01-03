from datetime import datetime, timedelta

import pytz
from courier.management.commands.send_in_next_five_mins import (
    check_for_unsent_user_messages, check_times, messagebox_pick, pick_message,
    which_messages)
from courier.models import UserSendTime
from django.core import mail, management
from django.test import TestCase
from freezegun import freeze_time
from fuauth.models import User
from messagebox.models import Message
from messagevault.models import CuratedMessage
from mock import patch


class TestSendInNextFiveMinutes(TestCase):
    """
    Tests the management command for sending the upcoming messages.
    """

    def setUp(self):
        names = [
            "Felicita",
            "Angela",
            "Robert",
            "Leonard",
            "Anthony",
            "Glen",
            "Lee",
            "Lorraine",
            "Heather",
            "Gary",
        ]
        for name in names:
            User.objects.create_user(
                name=name,
                phone_number="777-777-7777",
                carrier="ATT",
                password="password",
                user_timezone="HAWAII",
                email="{}@emailzzz.com".format(name),
            )

        past = datetime(2019, 12, 28, 1, 0, 0, tzinfo=pytz.UTC)

        future = datetime(2019, 12, 28, 22, 0, 0, tzinfo=pytz.UTC)

        # create 10 unsent send times in the future for all users

        for name in names:
            time = future
            for i in range(10):
                UserSendTime.objects.create(
                    scheduled_time=time, user=User.objects.get(name=name), sent=False
                )
                time = time + timedelta(minutes=1)

        # create 15 unsent send times in the past for all users

        for name in names:
            time = past
            for i in range(15):
                UserSendTime.objects.create(
                    scheduled_time=time, user=User.objects.get(name=name), sent=False
                )
                time = time + timedelta(minutes=1)

        # create 4 sent send times for all users

        for name in names:
            time = past + timedelta(seconds=30)
            for i in range(4):
                UserSendTime.objects.create(
                    scheduled_time=time, user=User.objects.get(name=name), sent=True
                )
                time = time + timedelta(minutes=1)

        # create unsent messages for Felicita and Angela

        self.felicita = User.objects.get(name="Felicita")
        self.angela = User.objects.get(name="Angela")
        self.robert = User.objects.get(name="Robert")

        for user in [self.felicita, self.angela]:
            Message.objects.create(
                recipient=user,
                sender_name="Test Sender",
                message_text="You're doing such a good job testing things!",
            )

        # create sent messages for Felicita and Angela

        for user in [self.felicita, self.angela]:
            Message.objects.create(
                recipient=user,
                sender_name="Test Sender",
                message_text="You're STILL doing such a good job testing things!",
                message_sent=True,
            )

        # create messages in the message vault

        CuratedMessage.objects.create(
            message_text="Things are wonderful!",
            message_author_first="Melanie",
            message_author_last="Crutchfield",
        )

    @freeze_time("2019-12-28 12:31")
    def test_check_times_all_unsent(self):
        """
        All send times in the past that are unsent should be returned.
        15 unsent past send times per user are created at setup
        """
        at_bat = check_times()
        assert len(at_bat) == 150

    @freeze_time("2019-12-31 12:31")
    def test_check_times_all_in_past(self):
        """
        If we move the current time to December 31st, all UserSendTimes should
        be returned unless they are sent.
        """
        at_bat = check_times()
        assert len(at_bat) == 250

    def test_which_messages(self):
        """
        If we run which_messages a bunch of times, it should pick both of the
        options eventually, but it should pick "messagevault" more often
        """
        result_list = []
        for run in range(500):
            result = which_messages()
            result_list.append(result)

        assert "messagevault" in result_list and "messagebox" in result_list
        assert result_list.count("messagevault") > (result_list.count("messagebox") * 2)

    def test_check_for_unsent_messages_user_has_messages(self):
        """
        If a user has unsent messages, check_for_unsent_messages should
        return True.
        """
        assert check_for_unsent_user_messages(self.felicita) is True
        assert check_for_unsent_user_messages(self.angela) is True
        assert check_for_unsent_user_messages(self.robert) is False

    def test_message_box_pick(self):
        """
        When a message is chosen from the message vault it should
        be returned concatenated with the sender's name, and the
        message should then be marked sent.

        """
        send_message, _ = messagebox_pick(self.felicita)

        assert (
            send_message == "You're doing such a good job testing things! -Test Sender"
        )

    @patch(
        "courier.management.commands.send_in_next_five_mins.which_messages",
        return_value="messagebox",
    )
    def test_pick_message_marks_message_sent(self, which_messages):
        """
        If a message is chosen from the messagebox, the message should be marked
        sent.
        """

        assert (
            len(Message.objects.filter(recipient=self.felicita, message_sent=False)) > 0
        )

        pick_message(self.felicita)

        assert (
            len(Message.objects.filter(recipient=self.felicita, message_sent=False))
            == 0
        )

    def test_pick_message_should_get_a_curated_message_if_user_has_no_custom_messages(
        self
    ):
        """
        If the user doesn't have any unsent custom messages it should choose
        one from the message vault.
        """
        message = pick_message(self.robert)
        assert message == "Things are wonderful! -Melanie Crutchfield"

    @patch(
        "courier.management.commands.send_in_next_five_mins.which_messages",
        return_value="messagevault",
    )
    def test_messagevault_pick(self, which_messages):
        """
        If the user has unsent custom messages but which_messages returns
        messagevault, a CuratedMessage should be chosen.
        """
        message = pick_message(self.angela)
        assert message == "Things are wonderful! -Melanie Crutchfield"

    @freeze_time("2019-12-28 12:31")
    def test_send_each_at_bat(self):
        """
        The management command should actually send some biz.
        """
        management.call_command("send_in_next_five_mins")
        assert len(mail.outbox) == 150
