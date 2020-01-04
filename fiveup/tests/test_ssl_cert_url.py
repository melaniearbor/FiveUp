from django.test import TestCase


class TestCertURL(TestCase):
    def test_url_gives_200(self):
        """
        The certificate view should receive a 200.
        """
        response = self.client.get(
            "/.well-known/pki-validation/BA7CD11C05866445FBFE053E2C1AAA8C.txt"
        )
        assert response.status_code == 200

    def test_cert_view_has_correct_content(self):
        """
        The certificate content should be correct.
        """
        response = self.client.get(
            "/.well-known/pki-validation/BA7CD11C05866445FBFE053E2C1AAA8C.txt"
        )

        cert_text = b"172DCB53812428BBE4077B6343FBD43719C8C85D599860CE17B66824DB9BDAFD comodoca.com 598504fd4f315"

        assert response.content == cert_text
