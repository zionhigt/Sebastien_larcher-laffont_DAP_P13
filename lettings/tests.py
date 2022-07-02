from django.test import TestCase
from django.urls import reverse

from lettings.models import Address, Letting


class LettingTestCase(TestCase):
    def setUp(self):
        self.mock_address = {
            "id": 1,
            "number": 2,
            "street": "test_street",
            "city": "test_city",
            "state": "test_state",
            "zip_code": 10000,
            "country_iso_code": "TEST_ISO",
        }
        Address.objects.create(**self.mock_address)

        self.mock_letting = {
            "id": 1,
            "title": "test_title",
            "address_id": 1,
        }
        Letting.objects.create(**self.mock_letting)

    def test_site_lettings_index_page(self):
        response = self.client.get(reverse("lettings_index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/index.html')
        self.assertContains(response, '<h1>Lettings</h1>')
        letting_html_link = "\n".join([
            f'<a href="/lettings/{self.mock_letting.get("id")}/">',
            f'                {self.mock_letting.get("title")}',
            '            </a>',
        ])
        self.assertContains(response, letting_html_link)

    def test_site_letings_letting_index_page(self):
        response = self.client.get(
            reverse("letting", kwargs={
                "letting_id": self.mock_letting.get("id"),
                }
            )
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/letting.html')
        self.assertContains(response, f'<h1>{self.mock_letting.get("title")}</h1>')
        letting_html_element = "\n".join([
            f'<p>{self.mock_address.get("number")} {self.mock_address.get("street")}</p>',
            #
            f'<p>{self.mock_address.get("city")}, {self.mock_address.get("state")} '\
            f'{self.mock_address.get("zip_code")}</p>',
            #
            f'<p>{self.mock_address.get("country_iso_code")}</p>',

        ])
        self.assertContains(response, letting_html_element)
