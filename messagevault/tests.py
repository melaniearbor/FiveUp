from django.test import TestCase

from .models import CuratedMessage


class TestMessageVault(TestCase):
    """
    Basic tests for the message vault.
    """

    def setUp(self):

        self.message = CuratedMessage.objects.create(
            message_text="You are beautiful",
            message_author_first="Melanie",
            message_author_last="Crutchfield",
        )

    def test_curatedmessage_string_repr(self):
        """
        The curated message object should have a nice string representation.
        """
        assert str(self.message) == "Crutchfield-You are beautiful"
