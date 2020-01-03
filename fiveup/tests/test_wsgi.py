from django.test import TestCase
from fiveup.wsgi import application


class TestWSGIApplication(TestCase):
    def test_application_sanity_check(self):
        assert application.request_class
        assert application.get_response
