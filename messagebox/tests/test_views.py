import uuid

from django.core.urlresolvers import reverse
from django.test import Client, TestCase
from functional_tests.utils import SeleniumTestCase


class TestMessageViews(SeleniumTestCase, TestCase):

    client = Client()

    def test_create_message_view(self):

        self.test_uuid = uuid.uuid4()
        response = self.client.get(reverse("add-message-view", args=[self.test_uuid]))
        assert response.status_code == 200


class TestMiscViews(SeleniumTestCase):
    def test_index(self):
        """
        Test the index view.
        """
        response = self.client.get(reverse("home"))
        assert response.status_code == 200

    def test_add_message_success(self):
        """
        Test the message success view.
        """
        response = self.client.get(reverse("add-message-success"))
        assert response.status_code == 200

    def test_contact(self):
        """
        Test the contact view.
        """
        response = self.client.get(reverse("contact"))
        assert response.status_code == 200
        assert "why don't ya" in response.content
        assert "www.twitter.com/hifiveup" in response.content
        assert "www.facebook.com/fiveupapp" in response.content
