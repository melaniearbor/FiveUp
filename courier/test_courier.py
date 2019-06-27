from fuauth.models import User
from management.commands import create_daily_schedule


def test_divide_users():
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
            email="{}@emailzzz.com".format(name)
        )
    group_a, group_b, group_c = create_daily_schedule.divid_users(User.objects.all())

    assert len(group_a) == 3
    assert len(group_b) == 3
    assert len(group_c) == 4
