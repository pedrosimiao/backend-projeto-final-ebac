from django.test import TestCase

from accounts.factories import UserFactory

from accounts.serializers.user_serializer import UserSerializer

class UserSerializerTest(TestCase):
    def test_serializer_output(self):
        user = UserFactory(username="tsygan")
        serializer = UserSerializer(user)
        
        self.assertEqual(serializer.data["username"], "tsygan")