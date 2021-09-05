from django.test import TestCase

from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_successful(self):
        email = 'test@rhizo.us'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_email_normalized(self):
        email = 'test@RHIZO.COM'
        user = get_user_model().objects.create_user(
            email=email,
        )
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Create new user with invalid email"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email=None, password='test123'
            )

    def test_create_new_superuser(self):
        """Create new superuser"""
        email = 'test@rhizo.us'
        password = 'testpass123'
        user = get_user_model().objects.create_superuser(
            email=email,
            password=password
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
