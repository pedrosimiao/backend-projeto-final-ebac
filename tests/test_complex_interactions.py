from rest_framework.test import APITestCase, APIClient
from django.urls import reverse

from accounts.factories import UserFactory
from posts.factories import PostFactory
from interactions.factories import LikeFactory, CommentFactory
from followers.factories import FollowerFactory

from accounts.models import User
from posts.models import Post
from interactions.models import Like, Comment
from followers.models import Follower

class ComplexInteractionsTest(APITestCase):
    def setUp(self):
        # Cria 5 usuários
        self.users = [UserFactory() for _ in range(5)]

        # Cada usuário cria 3 posts
        self.posts = []
        for user in self.users:
            self.posts.extend(PostFactory.create_batch(3, user=user))

        # Para cada post, o primeiro usuário curte e o segundo comenta
        self.likes = []
        self.comments = []
        for post in self.posts:
            liker = self.users[0]
            self.likes.append(LikeFactory(user=liker, post=post))
            commenter = self.users[1]
            self.comments.append(CommentFactory(user=commenter, post=post))

        # Cada usuário (exceto o último) segue o próximo na lista
        self.followers = []
        for i in range(len(self.users) - 1):
            self.followers.append(FollowerFactory(follower=self.users[i], following=self.users[i+1]))

        self.client = APIClient()
        # Autentica com o primeiro usuário para testar endpoints protegidos
        self.client.force_authenticate(user=self.users[0])

    def test_counts(self):
        # Verifica se os registros foram criados conforme esperado
        self.assertEqual(User.objects.count(), 5)
        self.assertEqual(Post.objects.count(), 5 * 3)
        self.assertEqual(Like.objects.count(), 5 * 3)
        self.assertEqual(Comment.objects.count(), 5 * 3)
        self.assertEqual(Follower.objects.count(), 4)

    def test_get_posts_endpoint(self):
        # Testa se o endpoint de posts retorna todos os posts criados
        url = reverse("posts-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), Post.objects.count())

    def test_like_post_endpoint(self):
        # Testa a criação de um like via API
        post = self.posts[0]
        url = reverse("likes-list")
        data = {"post": post.id, "user": self.users[0].id}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)

    def test_comment_post_endpoint(self):
        # Testa a criação de um comentário via API
        post = self.posts[1]
        url = reverse("comments-list")
        data = {"post": post.id, "user": self.users[0].id, "content": "Excelente post!"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)

    def test_create_retweet_endpoint(self):
        # Testa a criação de um retweet usando o campo write-only "retweet_id"
        original = PostFactory(content="Original Post for retweet")
        url = reverse("posts-list")
        data = {"content": "", "retweet_id": original.id}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)
        created_post = Post.objects.get(pk=response.data["id"])
        self.assertIsNotNone(created_post.retweet)
        self.assertEqual(created_post.retweet.id, original.id)
