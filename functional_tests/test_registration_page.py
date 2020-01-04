from django.core import mail
from fuauth.models import User

from .utils import SeleniumTestCase


class LoginTest(SeleniumTestCase):
    def test_registration_should_create_a_user(self):
        """
        We'll start with no users, register someone, and then end up
        with one user.
        """
        assert User.objects.all().count() == 0

        with self.wait_for_page_load():
            self.browser.get(self.live_server_url + "/")
        self.browser.find_element_by_name("name").send_keys("Melanie")
        self.browser.find_element_by_name("email").send_keys("test@gmailzzz.com")
        self.browser.find_element_by_name("phone_number").send_keys("6192222222")
        self.browser.find_element_by_name("carrier").send_keys("Virgin")
        self.browser.find_element_by_name("user_timezone").send_keys("Pacific")
        self.browser.find_element_by_name("password").send_keys("testpants")

        with self.wait_for_page_load():
            self.browser.find_element_by_css_selector("*[type=submit]").click()
        text = self.browser.find_element_by_tag_name("body").text

        assert "Want some more happy?" in text
        melanie = User.objects.all()[0]

        assert melanie.name == "Melanie"
        assert melanie.email == "test@gmailzzz.com"
        assert melanie.phone_number == "6192222222"
        assert melanie.carrier == "pixmbl.com"
        assert melanie.user_timezone == "PC"

    def test_registration_sends_confirmation_text(self):
        """
        A successful registration should trigger a welcome text.
        """
        with self.wait_for_page_load():
            self.browser.get(self.live_server_url + "/")
        self.browser.find_element_by_name("name").send_keys("Melanie")
        self.browser.find_element_by_name("email").send_keys("test@gmailzzz.com")
        self.browser.find_element_by_name("phone_number").send_keys("6192222222")
        self.browser.find_element_by_name("carrier").send_keys("Virgin")
        self.browser.find_element_by_name("user_timezone").send_keys("Pacific")
        self.browser.find_element_by_name("password").send_keys("testpants")
        with self.wait_for_page_load():
            self.browser.find_element_by_css_selector("*[type=submit]").click()

        assert len(mail.outbox) == 1

        message = mail.outbox[0]

        assert (
            "Hey there, partner! Hold on to your hat, because you're about to get lots of happy."
            in message.body
        )
        assert message.from_email == "Five Up <app44043297@heroku.com>"
        assert message.to == [u"6192222222@pixmbl.com"]
        assert message.subject == "FiveUp"

    def test_registration_form_invalid_javascript(self):
        """
        Test invalid email gives a warning message on screen. Done via javascript.
        """
        with self.wait_for_page_load():
            self.browser.get(self.live_server_url + "/")
        self.browser.find_element_by_name("name").send_keys("Melanie")
        self.browser.find_element_by_name("email").send_keys(
            "cass"
        )  # this isn't an email address!
        self.browser.find_element_by_name("phone_number").send_keys("6192222222")
        self.browser.find_element_by_name("carrier").send_keys("Virgin")
        self.browser.find_element_by_name("user_timezone").send_keys("Pacific")
        self.browser.find_element_by_name("password").send_keys("testpants")

        # We don't wait on this click because the page won't actually refresh since
        # the work is being done in javascript
        self.browser.find_element_by_css_selector("*[type=submit]").click()
        text = self.browser.find_element_by_tag_name("body").text
        assert "Hmm. Is that a real email address? Try again." in text
        assert User.objects.all().count() == 0

    def test_registration_form_invalid_server_side(self):
        """
        Test that a django-specific email error will toss us to the fallback
        registration page.
        """
        with self.wait_for_page_load():
            self.browser.get(self.live_server_url + "/")
        self.browser.find_element_by_name("name").send_keys("Melanie")
        self.browser.find_element_by_name("email").send_keys(
            "a@b.c"
        )  # this isn't an email address!
        self.browser.find_element_by_name("phone_number").send_keys("6192222222")
        self.browser.find_element_by_name("carrier").send_keys("Virgin")
        self.browser.find_element_by_name("user_timezone").send_keys("Pacific")
        self.browser.find_element_by_name("password").send_keys("testpants")
        with self.wait_for_page_load():
            self.browser.find_element_by_css_selector("*[type=submit]").click()
        assert self.browser.current_url == self.live_server_url + "/register/"
        assert User.objects.all().count() == 0

    def test_registration_with_get_method(self):
        """
        A GET should give a blank registration form and you should be able
        to submit the form.
        """
        assert User.objects.all().count() == 0

        with self.wait_for_page_load():
            self.browser.get(self.live_server_url + "/register/")
        self.browser.find_element_by_name("name").send_keys("Melanie")
        self.browser.find_element_by_name("email").send_keys("test@gmailzzz.com")
        self.browser.find_element_by_name("phone_number").send_keys("6192222222")
        self.browser.find_element_by_name("carrier").send_keys("Virgin")
        self.browser.find_element_by_name("user_timezone").send_keys("Pacific")
        self.browser.find_element_by_name("password").send_keys("testpants")

        with self.wait_for_page_load():
            self.browser.find_element_by_css_selector("*[type=submit]").click()

        text = self.browser.find_element_by_tag_name("body").text

        assert "Want some more happy?" in text
        melanie = User.objects.all()[0]

        assert melanie.name == "Melanie"
        assert melanie.email == "test@gmailzzz.com"
        assert melanie.phone_number == "6192222222"
        assert melanie.carrier == "pixmbl.com"
        assert melanie.user_timezone == "PC"
