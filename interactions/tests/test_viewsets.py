from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from interactions.factories import LikeFactory, CommentFactory


class InteractionViewSetTest(APITestCase):
    def setUp(self):
        self.client = APIClient()

        from accounts.factories import UserFactory

        self.user = UserFactory()
        self.client.force_authenticate(user=self.user)

        self.like_url = reverse("likes-list")
        self.comment_url = reverse("comments-list")

    def test_create_like_api(self):
        data = {"post": LikeFactory().post.id, "user": self.user.id}
        response = self.client.post(self.like_url, data)
        self.assertEqual(response.status_code, 201)

    def test_create_comment_api(self):
        data = {
            "post": CommentFactory().post.id,
            "user": self.user.id,
            "content": "Awesome!",
        }
        response = self.client.post(self.comment_url, data)
        self.assertEqual(response.status_code, 201)
