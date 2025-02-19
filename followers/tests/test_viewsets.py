from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from followers.factories import FollowerFactory
from accounts.factories import UserFactory


class FollowerViewSetTest(APITestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = UserFactory()
        self.client.force_authenticate(user=self.user)

        self.url = reverse("followers-list")

    def test_create_follower_api(self):
        other_user = UserFactory()
        data = {"follower": self.user.id, "following": other_user.id}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 201)
