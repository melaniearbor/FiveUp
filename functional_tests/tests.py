from utils import SeleniumTestCase


class TestBasicPages(SeleniumTestCase):

    def test_home_page_renders(self):
        """
        Tests that the home url renders and has some text in it.
        """
        self.browser.get(self.live_server_url)
        assert "FiveUp" in self.browser.title
        text = self.browser.find_element_by_tag_name("body").text
        assert "How it works" in text
