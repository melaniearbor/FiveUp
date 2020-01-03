import uuid

from django.core.urlresolvers import reverse
from django.test import Client, TestCase
from fuauth.models import User
from functional_tests.utils import SeleniumTestCase

from ..models import Message


class TestMessageViews(SeleniumTestCase):

    client = Client()

    def setUp(self):

        self.noofie = User.objects.create_user(
            name="Noofie",
            phone_number="777-777-7777",
            carrier="ATT",
            password="password",
            user_timezone="HAWAII",
            email="noofie@emailzzz.com",
        )

    def test_create_message_view(self):

        """
        Test that the create message view renders.
        """

        self.test_uuid = uuid.uuid4()
        response = self.client.get(reverse("add-message-view", args=[self.test_uuid]))
        assert response.status_code == 200

    def test_a_message_can_be_created_for_a_user(self):

        """
        A message should be able to be created for a specific user.
        """

        with self.wait_for_page_load():
            self.browser.get(self.live_server_url + "/new/" + str(self.noofie.uuid))

        text = self.browser.find_element_by_tag_name("body").text
        assert "Send Noofie some happy!" in text

        self.browser.find_element_by_name("sender_name").send_keys("Moof")
        self.browser.find_element_by_name("message_text").send_keys(
            "You're doing wonderful. It's okay to struggle."
        )
        with self.wait_for_page_load():
            self.browser.find_element_by_css_selector("*[type=submit]").click()

        assert "500" not in self.browser.find_element_by_tag_name("body").text
        noof_message = Message.objects.get(recipient=self.noofie)
        assert (
            noof_message.message_text
            == "You're doing wonderful. It's okay to struggle."
        )
        assert noof_message.message_sent is False
        assert noof_message.sender_name == "Moof"

    def test_a_create_message_for_missing_user(self):

        """
        Submitting a message for a non-existent user redirects to the index.
        """

        self.rando_uuid = uuid.uuid4()
        with self.wait_for_page_load():
            self.browser.get(self.live_server_url + "/new/" + str(self.rando_uuid))

        self.browser.find_element_by_name("sender_name").send_keys("Moof")
        self.browser.find_element_by_name("message_text").send_keys(
            "Who am I sending this to? No one! That's silly!"
        )

        with self.wait_for_page_load():
            self.browser.find_element_by_css_selector("*[type=submit]").click()
        assert self.browser.current_url == self.live_server_url + "/"

        assert "500" not in self.browser.find_element_by_tag_name("body").text


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
