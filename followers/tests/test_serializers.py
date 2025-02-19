from django.test import TestCase
from followers.factories import FollowerFactory
from followers.serializers.follower_serializer import FollowerSerializer


class FollowerSerializerTest(TestCase):
    def test_follower_serializer(self):
        follow = FollowerFactory()
        serializer = FollowerSerializer(follow)
        self.assertEqual(serializer.data["follower"], follow.follower.id)
