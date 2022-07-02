from django.test import TestCase
from django.urls import reverse

from django.contrib.auth.models import User
from profiles.models import Profile


class ProfileTestCase(TestCase):
    def setUp(self):
        self.mock_user = {
            "id": 1,
            "username": 'test_username',
            "first_name": 'test_firstname',
            "last_name": 'test_lastname',
            "email": 'test_email',
        }
        User.objects.create(**self.mock_user)

        self.mock_profile = {
            "id": 1,
            'favorite_city': "test_favorite_city",
            'user_id': 1,

        }
        Profile.objects.create(**self.mock_profile)

    def test_site_profiles_index_page(self):
        response = self.client.get(reverse("profiles_index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/index.html')
        self.assertContains(response, '<h1>Profiles</h1>')
        profile_html_link = "\n".join([
            f'<a href="/profiles/{self.mock_user.get("username")}/">',
            f'                {self.mock_user.get("username")}',
            '            </a>',
        ])
        self.assertContains(response, profile_html_link)

    def test_site_profiles_profile_page(self):
        response = self.client.get(
            reverse("profile", kwargs={
                "username": self.mock_user.get("username"),
                }
            )
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')
        self.assertContains(response, f'<h1>{self.mock_user.get("username")}</h1>')
        profile_html_element = "\n".join([
            f'<p>First name: {self.mock_user.get("first_name")}</p>',
            f'<p>Last name: {self.mock_user.get("last_name")}</p>',
            f'<p>Email: {self.mock_user.get("email")}</p>',
            f'<p>Favorite city: {self.mock_profile.get("favorite_city")}</p>',

        ])
        self.assertContains(response, profile_html_element)
