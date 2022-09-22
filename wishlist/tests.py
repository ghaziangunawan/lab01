from django.test import TestCase

# Create your tests here.
class KatalogTest(TestCase):
    def test_url(self):
        resp = self.client.get('/wishlist/')
        self.assertEqual(resp.status_code, 200)

    def test_template(self):
        resp = self.client.get('/wishlist/')
        self.assertTemplateUsed(resp, 'wishlist.html')
