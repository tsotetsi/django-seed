from django.test import TestCase

URLS_PUBLIC = [
    "/admin/",
]


class SimpleTests(TestCase):
    def test_urls(self):
        for url in URLS_PUBLIC:
            res = self.client.get(url)
            self.assertEqual(res.status_code, 302)
