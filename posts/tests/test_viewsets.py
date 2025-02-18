from rest_framework.test import APITestCase, APIClient
from django.urls import reverse

from accounts.factories import UserFactory
from posts.factories import PostFactory

from posts.models.post import Post

class PostViewSetTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        # Cria e autentica um usuário
        self.user = UserFactory()
        self.client.force_authenticate(user=self.user)
        self.url = reverse("posts-list")

    def test_create_post(self):
        data = {"content": "Test Post"}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Post.objects.count(), 1)

    def test_create_retweet(self):
        original = PostFactory(content="Original Post")
        data = {"content": "", "retweet_id": original.id}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 201)
        created_post = Post.objects.get(pk=response.data["id"])
        self.assertIsNotNone(created_post.retweet)
