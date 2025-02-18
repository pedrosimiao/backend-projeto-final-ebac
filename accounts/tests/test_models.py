from django.test import TestCase

from accounts.factories import UserFactory

from accounts.models.user import User

class UserModelTest(TestCase):
    def test_create_user(self):
        user = UserFactory()

        self.assertIsNotNone(user.pk)
        self.assertTrue(user.check_password("123456"))