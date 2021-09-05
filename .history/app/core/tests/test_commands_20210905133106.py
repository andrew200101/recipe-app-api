from unittest.mock import patch
from django.core.management import call_command
from django.db.utils import OperationalErros
from django.test import TestCase


class CommandTests(TestCase):
    def test_wait_for_db_ready
