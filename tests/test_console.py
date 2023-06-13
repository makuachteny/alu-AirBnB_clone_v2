#!/usr/bin/python3


import unittest


from console import HBNBCommand
from unittest.mock import patch
from io import StringIO
from models import storage
import os

stdout = StringIO()
console = HBNBCommand()


class ConsoleTestCase(unittest.TestCase):

    def test_create(self):
        if os.getenv("HBNB_TYPE_STORAGE") != "db":
            with patch('sys.stdout', stdout):
                console.onecmd('create State name="california"')
            self.assertEqual(len(stdout.getvalue()), 36)
