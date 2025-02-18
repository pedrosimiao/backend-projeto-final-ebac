from django.test import TestCase
from interactions.factories import LikeFactory, CommentFactory
from interactions.serializers.like_serializer import LikeSerializer
from interactions.serializers.comment_serializer import CommentSerializer

class InteractionSerializerTest(TestCase):
    def test_like_serializer(self):
        like = LikeFactory()
        serializer = LikeSerializer(like)
        self.assertEqual(serializer.data["post"], like.post.id)

    def test_comment_serializer(self):
        comment = CommentFactory(content="Elon sucks!")
        serializer = CommentSerializer(comment)
        self.assertEqual(serializer.data["content"], "Elon sucks!")
