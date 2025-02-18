from rest_framework.test import APITestCase, APIClient
from django.urls import reverse

from accounts.factories import UserFactory

class UserViewSetTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = UserFactory()
        self.client.force_authenticate(user=self.user)
        self.url = reverse("users-list")

    def test_get_users(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)