from django.test import TestCase

URLS_PUBLIC = [
    "/",
]


class SimpleTests(TestCase):
    def test_urls(self):
        for url in URLS_PUBLIC:
            res = self.client.get(url)
            self.assertEqual(res.status_code, 200)
