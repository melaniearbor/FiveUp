from fuauth.models import User

from .utils import SeleniumTestCase


class LoginTest(SeleniumTestCase):
    def setUp(self):
        User.objects.create_user(
            "Melanie",
            "6192222222",
            User.ATT,
            User.HAWAII,
            email="test@gmail.com",
            password="testpants",
        )

    def test_successful_login(self):
        with self.wait_for_page_load():
            self.browser.get(self.live_server_url + "/login/")
        self.browser.find_element_by_name("username").send_keys("test@gmail.com")
        self.browser.find_element_by_name("password").send_keys("testpants")
        with self.wait_for_page_load():
            self.browser.find_element_by_css_selector("*[type=submit]").click()
        text = self.browser.find_element_by_tag_name("body").text
        self.assertIn("Hi " + "Melanie" + ".", text)

    def test_unsuccessful_login(self):
        self.browser.get(self.live_server_url + "/login/")
        self.browser.find_element_by_name("username").send_keys("test@gmail.com")
        self.browser.find_element_by_name("password").send_keys("notgonnawork")
        with self.wait_for_page_load():
            self.browser.find_element_by_css_selector("*[type=submit]").click()
        text = self.browser.find_element_by_tag_name("body").text
        self.assertIn("Please enter a correct your email address and password", text)
