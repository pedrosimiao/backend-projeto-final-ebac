from django.test import TestCase
from followers.factories import FollowerFactory


class FollowerModelTest(TestCase):
    def test_create_follower(self):
        follow = FollowerFactory()
        self.assertIsNotNone(follow.pk)
