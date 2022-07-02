from django.test import TestCase
from django.urls import reverse

class IndexTestCase(TestCase):
    def setUp(self):
        super().setUp()
    
    def test_site_index_page(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
        self.assertContains(response, '<h1>Welcome to Holiday Homes</h1>')


    