from django.test import TestCase

from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_successful(self):
        email = 'test@rhizo.us'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.checkpassword(password))
