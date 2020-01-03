from collections import OrderedDict

from fuauth.models import User
from selenium.webdriver.support.select import Select
from utils import SeleniumTestCase


class TestChangeProfile(SeleniumTestCase):
    def setUp(self):

        User.objects.create_user(
            "Melanie",
            "6192222222",
            User.ATT,
            User.HAWAII,
            email="test@gmail.com",
            password="testpants",
        )

        User.objects.create_user(
            "Barack",
            "7778889999",
            User.ATT,
            User.HAWAII,
            email="b@zzzzzarg.com",
            password="testslacks",
        )

    def test_user_can_change_their_phone_number(self):
        """
        A user should be able to change their profile.
        """
        melanie = User.objects.get(name="Melanie")

        with self.wait_for_page_load():
            self.browser.get(self.live_server_url + "/login/")
        self.browser.find_element_by_name("username").send_keys("test@gmail.com")
        self.browser.find_element_by_name("password").send_keys("testpants")
        with self.wait_for_page_load():
            self.browser.find_element_by_css_selector("*[type=submit]").click()

        self.browser.get(
            self.live_server_url + "/changeprofile/" + str(melanie.uuid) + "/"
        )
        text = self.browser.find_element_by_tag_name("body").text
        assert "Change your deets, Melanie" in text

        self.browser.find_element_by_name("phone_number").clear()
        self.browser.find_element_by_name("phone_number").send_keys("7777777772")
        with self.wait_for_page_load():
            self.browser.find_element_by_css_selector("*[type=submit]").click()

        melanie = User.objects.get(name="Melanie")

        assert melanie.phone_number == "7777777772"

    def test_user_can_change_their_carrier(self):
        """
        A user should be able to change their carrier.
        """
        melanie = User.objects.get(name="Melanie")

        with self.wait_for_page_load():
            self.browser.get(self.live_server_url + "/login/")
        self.browser.find_element_by_name("username").send_keys("test@gmail.com")
        self.browser.find_element_by_name("password").send_keys("testpants")
        self.browser.find_element_by_css_selector("*[type=submit]").click()

        carrier_indexes = dict(enumerate(OrderedDict(User.CARRIER_CHOICES).keys()))
        for index in carrier_indexes:
            with self.wait_for_page_load():
                self.browser.get(
                    self.live_server_url + "/changeprofile/" + str(melanie.uuid) + "/"
                )

            with self.wait_for_page_load():
                carrier = self.browser.find_element_by_name("carrier")
                selector = Select(self.browser.find_element_by_name("carrier"))
                carrier.click()
                selector.select_by_index(index)
                carrier.click()
                self.browser.find_element_by_css_selector("*[type=submit]").click()

            melanie = User.objects.get(name="Melanie")

            assert melanie.carrier == carrier_indexes[index]

    def test_user_can_change_their_timezone(self):
        """
        A user should be able to change their timezone.
        """
        melanie = User.objects.get(name="Melanie")

        with self.wait_for_page_load():
            self.browser.get(self.live_server_url + "/login/")
        self.browser.find_element_by_name("username").send_keys("test@gmail.com")
        self.browser.find_element_by_name("password").send_keys("testpants")
        with self.wait_for_page_load():
            self.browser.find_element_by_css_selector("*[type=submit]").click()

        timezone_indexes = dict(enumerate(OrderedDict(User.TIME_ZONE_CHOICES).keys()))
        for index in timezone_indexes:
            with self.wait_for_page_load():
                self.browser.get(
                    self.live_server_url + "/changeprofile/" + str(melanie.uuid) + "/"
                )

            timezone = self.browser.find_element_by_name("user_timezone")
            selector = Select(self.browser.find_element_by_name("user_timezone"))
            timezone.click()
            selector.select_by_index(index)
            timezone.click()
            with self.wait_for_page_load():
                self.browser.find_element_by_css_selector("*[type=submit]").click()

            melanie = User.objects.get(name="Melanie")

            assert melanie.user_timezone == timezone_indexes[index]

    def test_user_can_change_their_message_amounts(self):
        """
        A user should be able to change how many messages they receive.
        """
        melanie = User.objects.get(name="Melanie")

        with self.wait_for_page_load():
            self.browser.get(self.live_server_url + "/login/")
        self.browser.find_element_by_name("username").send_keys("test@gmail.com")
        self.browser.find_element_by_name("password").send_keys("testpants")
        self.browser.find_element_by_css_selector("*[type=submit]").click()

        message_number_indexes = dict(
            enumerate(OrderedDict(User.HOW_MANY_MESSAGES_CHOICES).keys())
        )
        for index in message_number_indexes:
            with self.wait_for_page_load():
                self.browser.get(
                    self.live_server_url + "/changeprofile/" + str(melanie.uuid) + "/"
                )

            with self.wait_for_page_load():
                message_number = self.browser.find_element_by_name("how_many_messages")
                selector = Select(
                    self.browser.find_element_by_name("how_many_messages")
                )
                message_number.click()
                selector.select_by_index(index)
                message_number.click()
                self.browser.find_element_by_css_selector("*[type=submit]").click()

            melanie = User.objects.get(name="Melanie")

            assert melanie.how_many_messages == message_number_indexes[index]

    def test_user_can_stop_receiving_messages(self):

        """
        A user should be able to stop receiving messages, and resume receiving messages.
        """

        melanie = User.objects.get(name="Melanie")

        with self.wait_for_page_load():
            self.browser.get(self.live_server_url + "/login/")
        self.browser.find_element_by_name("username").send_keys("test@gmail.com")
        self.browser.find_element_by_name("password").send_keys("testpants")
        self.browser.find_element_by_css_selector("*[type=submit]").click()

        with self.wait_for_page_load():
            self.browser.get(
                self.live_server_url + "/changeprofile/" + str(melanie.uuid) + "/"
            )

        with self.wait_for_page_load():
            receiving = self.browser.find_element_by_name("receiving_messages")
            receiving.click()
            self.browser.find_element_by_css_selector("*[type=submit]").click()

        melanie = User.objects.get(name="Melanie")

        assert melanie.receiving_messages is False

        with self.wait_for_page_load():
            self.browser.get(
                self.live_server_url + "/changeprofile/" + str(melanie.uuid) + "/"
            )

        with self.wait_for_page_load():
            receiving = self.browser.find_element_by_name("receiving_messages")
            receiving.click()
            self.browser.find_element_by_css_selector("*[type=submit]").click()

        melanie = User.objects.get(name="Melanie")

        assert melanie.receiving_messages is True

    def test_users_cannot_change_other_users_details(self):
        """
        Users should not be able to change other users details.
        """
        barack = User.objects.get(name="Barack")

        # log Melanie in
        with self.wait_for_page_load():
            self.browser.get(self.live_server_url + "/login/")
        self.browser.find_element_by_name("username").send_keys("test@gmail.com")
        self.browser.find_element_by_name("password").send_keys("testpants")

        with self.wait_for_page_load():
            self.browser.find_element_by_css_selector("*[type=submit]").click()

        # try to change Barack's details
        self.browser.get(
            self.live_server_url + "/changeprofile/" + str(barack.uuid) + "/"
        )

        assert self.browser.current_url == self.live_server_url + "/login/"

        assert barack.receiving_messages is True

    def test_anonymous_users_cannot_change_details(self):

        """
        Anonymous users should be redirected to login when they hit the
        change profile url
        """
        barack = User.objects.get(name="Barack")

        # try to change Barack's details
        self.browser.get(
            self.live_server_url + "/changeprofile/" + str(barack.uuid) + "/"
        )

        assert self.browser.current_url == self.live_server_url + "/login/"

        assert barack.receiving_messages is True
