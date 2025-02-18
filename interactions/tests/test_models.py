from django.test import TestCase
from interactions.factories import LikeFactory, CommentFactory

class InteractionModelTest(TestCase):
    def test_create_like(self):
        like = LikeFactory()
        self.assertIsNotNone(like.pk)

    def test_create_comment(self):
        comment = CommentFactory(content="Nice post!")
        self.assertIsNotNone(comment.pk)
        self.assertEqual(comment.content, "Nice post!")
