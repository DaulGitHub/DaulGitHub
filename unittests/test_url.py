from unittest import TestCase
from url import CreateShortURL
import re


class TestCreateShortURL(TestCase):

    def setUp(self) -> None:
        self.url = CreateShortURL('http', 'localhost')

    def test_get_url_check_len(self):
        short = self.url.get_url()

        url_len = 23
        self.assertEqual(len(short), url_len)

    def test_get_url_contain_protocol_domain(self):
        short = self.url.get_url()

        self.assertTrue("http://localhost" in short)

    def test_check_get_url_check_prefix(self):
        short = self.url.get_url()

        self.assertEqual(short[-7], '/')
        prefix = short[-6:]
        find = re.findall('^\w+$', prefix)
        self.assertEqual(len(find), 1, f"Prefix contains special symbols. Prifix is: {prefix}")
