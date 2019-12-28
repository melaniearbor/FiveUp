import pytest
from django.test import TestCase

from .models import User


class TestUserModel(TestCase):
    def test_a_user_can_be_created(self):
        """
        Creating a regular user should give them
        regular permissions.
        """
        ag = User.objects.create_user(
            name="A.G.",
            phone_number="777-777-7777",
            carrier="ATT",
            password="password",
            user_timezone="HAWAII",
            email="ag@emailzzzz.nerf",
        )
        assert ag.is_active is True
        assert ag.is_staff is False
        assert ag.is_superuser is False

    def test_user_needs_email(self):
        """
        A user needs to supply an email address.
        """
        with pytest.raises(ValueError):
            User.objects.create_user(
                name="Melanie",
                phone_number="777-777-7777",
                carrier="ATT",
                password="password",
                user_timezone="HAWAII",
                email="",
            )

    def test_create_super_user(self):
        """
        Creating a super user should make them super.
        """

        super_melanie = User.objects.create_superuser(
            name="Melanie",
            phone_number="777-777-7777",
            carrier="ATT",
            password="password",
            user_timezone="HAWAII",
            email="supermelanie@emailzzzz.nerf",
        )

        assert super_melanie.is_active is True
        assert super_melanie.is_staff is True
        assert super_melanie.is_superuser is True

    def test_a_string_representations(self):
        """
        We should be able to get first name and short names
        off a user
        """
        amanda = User.objects.create_user(
            name="Amanda",
            phone_number="777-777-7777",
            carrier="ATT",
            password="password",
            user_timezone="HAWAII",
            email="amanda@emailzzzz.nerf",
        )
        assert amanda.get_full_name() == "Amanda"
        assert amanda.get_short_name() == "Amanda"
