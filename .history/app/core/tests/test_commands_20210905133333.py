from unittest.mock import patch
from django.core.management import call_command
from django.db.utils import OperationalErros
from django.test import TestCase


class CommandTests(TestCase):
    def test_wait_for_db_ready(self):
        with patch('django.db.utils.ConnectionHandler.__getitem__') as get_item:
            get_item.return_value = True
