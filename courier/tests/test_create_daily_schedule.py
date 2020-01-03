import datetime

from courier.management.commands import create_daily_schedule
from courier.models import UserSendTime
from django.core import management
from django.test import TestCase
from fuauth.models import User


class TestDailySchedule(TestCase):
    """
    Tests for creating the daily schedule for message sending.
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

    def test_divide_users(self):
        """
        Test that three groups are created evenly with the remainder
        left to the last group.
        """
        group_a = []
        group_b = []
        group_c = []
        group_a, group_b, group_c = create_daily_schedule.divide_users(
            group_a, group_b, group_c
        )

        assert len(group_a) == 3
        assert len(group_b) == 3
        assert len(group_c) == 4

    def test_create_schedule(self):
        """
        Test that five send times are created.
        """
        schedule = create_daily_schedule.create_schedule()
        assert len(schedule) == 5

    def test_schedule_date(self):
        """
        Test that all send times are for the current day
        """
        schedule = create_daily_schedule.create_schedule()
        send_time_dates = [send_time.date() for send_time in schedule]
        for date in send_time_dates:
            assert date == datetime.date.today()

    def test_schedule_is_spread_out(self):
        """
        Test that send times are no closer together than 40 minutes and
        no farther apart than 2 hours and 36 minutes.
        """
        schedule = create_daily_schedule.create_schedule()
        send_times = [send_time for send_time in schedule]
        spreads = []
        for time in send_times:
            if send_times.index(time) != 4:
                spread = send_times[send_times.index(time) + 1] - time
            spreads.append(spread.seconds)
        assert max(spreads) < 9361
        assert min(spreads) > 2399

    def test_active_user_send_times(self):
        """
        An active user with default number of messages should
        get 5 send times scheduled.
        """

        fel = User.objects.get(name="Felicita")
        ang = User.objects.get(name="Angela")
        rob = User.objects.get(name="Robert")
        group = [fel, ang, rob]
        create_daily_schedule.record_user_send_times(group)
        assert UserSendTime.objects.filter(user=fel).count() == 5

    def test_user_wants_n_messages(self):
        """
        If a user only wants n messages they should only have
        n messages scheduled.
        """

        fel = User.objects.get(name="Felicita")
        ang = User.objects.get(name="Angela")
        rob = User.objects.get(name="Robert")
        group = [fel, ang, rob]
        for n in range(1, 6):
            fel.how_many_messages = n
            fel.save()
            create_daily_schedule.record_user_send_times(group)
            assert UserSendTime.objects.filter(user=fel).count() == n
            UserSendTime.objects.filter(user=fel).delete()

    def test_create_daily_schedule_management_commands(self):
        """
        Running the create_daily_schedule management command
        should result in 5 send times per user.
        """
        management.call_command("create_daily_schedule")
        assert UserSendTime.objects.all().count() == 50
