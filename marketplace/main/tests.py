from django.test import TestCase


class TestItem(TestCase):

    def test_explore(self):
        response = self.client.get('/explore/')
        self.assertEqual(response.status_code, 200)
