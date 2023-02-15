import unittest
from unittest.mock import Mock
class SomeTextCorrector:
     def __init__(self, items, id=None):
         self.items = items
     def correct(self, text_object):
         temp_str = text_object.original_text
         for substring in self.items["trash_substrings"]:
             if substring in temp_str:
                 temp_str = temp_str.replace(substring, "")
         text_object.original_text = temp_str.strip()
         return text_object
class TestSomeTextCorrector(unittest.TestCase):
     @classmethod
     def setUpClass(cls):
         items = {
         'trash_substrings': ["spam", "credit"]
         }
         cls.filter = SomeTextCorrector(items)
     def test_1(self):
         text_object = Mock()
         text_object.original_text = "spam always comes in to get a loan"
         result = TestSomeTextCorrector.filter.correct(text_object)
         self.assertEqual('always comes when possible to take', result.original_text)
if __name__ == '__main__':
     unittest.main()