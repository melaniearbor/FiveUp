from fuauth.models import User
from utils import SeleniumTestCase


class LogoutTest(SeleniumTestCase):
    def setUp(self):
        User.objects.create_user(
            "Melanie",
            "6192222222",
            User.ATT,
            User.HAWAII,
            email="test@gmail.com",
            password="testpants",
        )

    def test_successful_logout(self):

        # first login
        with self.wait_for_page_load():
            self.browser.get(self.live_server_url + "/login/")
        self.browser.find_element_by_name("username").send_keys("test@gmail.com")
        self.browser.find_element_by_name("password").send_keys("testpants")
        with self.wait_for_page_load():
            self.browser.find_element_by_css_selector("*[type=submit]").click()

        # then logout
        with self.wait_for_page_load():
            self.browser.find_element_by_xpath('//a[@href="/logoutuser/"]').click()
        text = self.browser.find_element_by_tag_name("body").text
        assert "Goodbye, you" in text
        assert " day!" in text

        with self.wait_for_page_load():
            self.browser.get(self.live_server_url + "/login/")
        text = self.browser.find_element_by_tag_name("body").text
        assert (
            "Copy/paste to share your link with your internet friendsies." not in text
        )
        assert "Log your little gourd in." in text
