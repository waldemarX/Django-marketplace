from django.test import TestCase


class TestItem(TestCase):

    def test_create(self):
        response = self.client.get('/p/create/')
        self.assertEqual(response.status_code, 200)
