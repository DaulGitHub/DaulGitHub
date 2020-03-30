from unittest import TestCase
from url import CreateShortURL
import re


class TestCreateShortURL(TestCase):

    def setUp(self) -> None:
        self.protocol = 'http'
        self.host = 'localhost'
        self.port = '5000'
        self.url = CreateShortURL(self.protocol, self.host, self.port)

    def test_get_url_contain_protocol_domain(self):
        short = self.url.get_url("qweRt1")

        self.assertEqual("http://localhost:5000/qweRt1", short)

    def test_check_get_url_check_prefix(self):
        short = self.url.get_url("qweRt1")

        self.assertEqual(short[-7], '/')
        prefix = short[-6:]
        find = re.findall('^\w+$', prefix)
        self.assertEqual(len(find), 1, f"Prefix contains special symbols. Prifix is: {prefix}")
