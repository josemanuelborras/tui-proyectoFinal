from django.test import TestCase
from django.urls import reverse

class IndexViewTests(TestCase):
    def test_index_contains_login_links(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        admin_url = reverse('admin_login')
        alumno_url = reverse('alumno_login')
        self.assertContains(resp, f'href="{admin_url}"')
        self.assertContains(resp, f'href="{alumno_url}"')
