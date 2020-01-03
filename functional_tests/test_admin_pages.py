from courier.models import UserSendTime
from fuauth.models import User
from functional_tests.utils import SeleniumTestCase


class TestAdmin(SeleniumTestCase):
    """
    Tests for the FiveUp admin dashboard.
    """

    def setUp(self):

        self.admin_user = User.objects.create_superuser(
            name="Noofie Admin",
            phone_number="777-777-7777",
            carrier="ATT",
            password="password",
            user_timezone="HAWAII",
            email="noofie@emailzzz.com",
        )

        self.plain_jane = User.objects.create_user(
            name="Jane",
            phone_number="777-777-7771",
            carrier="ATT",
            password="password1",
            user_timezone="HAWAII",
            email="plain_jane@emailzzz.com",
        )

        self.plain_jane_send_time = UserSendTime.objects.create(user=self.plain_jane)

    def test_non_admin_cannot_log_in(self):
        """
        Non-admin users should not be able to login to the admin page.
        """

        with self.wait_for_page_load():
            self.browser.get(self.live_server_url + "/admin/")
        self.browser.find_element_by_name("username").send_keys(self.plain_jane.email)
        self.browser.find_element_by_name("password").send_keys("password")
        with self.wait_for_page_load():
            self.browser.find_element_by_css_selector("*[type=submit]").click()
        text = self.browser.find_element_by_tag_name("body").text

        warning = "Please enter the correct your email address and password for a staff account. Note that both fields may be case-sensitive."
        assert warning in text

    def test_admin_page_renders_for_admin_user(self):
        """
        Test that the admin interface renders.
        """

        with self.wait_for_page_load():
            self.browser.get(self.live_server_url + "/admin/")
        self.browser.find_element_by_name("username").send_keys(self.admin_user.email)
        self.browser.find_element_by_name("password").send_keys("password")
        with self.wait_for_page_load():
            self.browser.find_element_by_css_selector("*[type=submit]").click()
        text = self.browser.find_element_by_tag_name("body").text

        page_items = [
            "Django administration",
            "Welcome, Noofie Admin.",
            "Change password / Log out",
            "Site administration",
            "Groups",
            "Courier",
            "Email log",
            "Fuauth",
            "Messages",
            "Curated messages",
        ]

        for item in page_items:
            assert item in text

    def test_custom_user_admin(self):
        """
        Test the send time admin
        """

        with self.wait_for_page_load():
            self.browser.get(self.live_server_url + "/admin/")
        self.browser.find_element_by_name("username").send_keys(self.admin_user.email)
        self.browser.find_element_by_name("password").send_keys("password")
        with self.wait_for_page_load():
            self.browser.find_element_by_css_selector("*[type=submit]").click()
        with self.wait_for_page_load():
            self.browser.find_element_by_link_text("Users").click()
        text = self.browser.find_element_by_tag_name("body").text
        assert "noofie@emailzzz.com" in text
        assert "Noofie Admin" in text
        assert "plain_jane@emailzzz.com" in text
        assert "Jane" in text
        assert "2 users" in text

    def test_send_time_admin(self):
        """
        Test the send time admin
        """

        with self.wait_for_page_load():
            self.browser.get(self.live_server_url + "/admin/")
        self.browser.find_element_by_name("username").send_keys(self.admin_user.email)
        self.browser.find_element_by_name("password").send_keys("password")
        with self.wait_for_page_load():
            self.browser.find_element_by_css_selector("*[type=submit]").click()
        with self.wait_for_page_load():
            self.browser.find_element_by_link_text("User send times").click()
        text = self.browser.find_element_by_tag_name("body").text
        assert "plain_jane@emailzzz.com" in text
        assert "Jane" in text
