from django.test import TestCase
from posts.factories import PostFactory
from posts.serializers.post_serializer import PostSerializer


class PostSerializerTest(TestCase):
    def test_serializer_without_retweet(self):
        post = PostFactory(content="Hello World")
        serializer = PostSerializer(post)
        self.assertEqual(serializer.data["content"], "Hello World")
        self.assertIsNone(serializer.data["retweet"])

    def test_serializer_with_retweet(self):
        original_post = PostFactory(content="Original Post")
        retweet = PostFactory(retweet=original_post, content="")
        serializer = PostSerializer(retweet)
        self.assertIsNotNone(serializer.data["retweet"])
        self.assertEqual(serializer.data["retweet"]["id"], original_post.id)
