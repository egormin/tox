from unittest import TestCase
from tag_counter.core import get_message

class HelloworldTestCase(TestCase):
    def test_helloworld(self):
        self.assertEqual(get_message(), 'Hello World!')
        
    def test_helloworld1(self):
        self.assertEqual(get_message(), 'Hello World!')
        
    def test_helloworld2(self):
        self.assertEqual(get_message(), 'Hello World!1')

