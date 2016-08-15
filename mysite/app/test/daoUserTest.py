
import unittest.mock
from unittest import mock
from unittest.mock import MagicMock

from django.core.urlresolvers import reverse
from django.test import Client

client = Client()

class TestStringMethods(unittest.TestCase):


    def test_insertUserInMongo(self):
        self.client = Client()
        response = self.client.get(reverse('app:index'))
        self.assertEqual(response.status_code, 200)


    def test_isupper(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()