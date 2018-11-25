import unittest
from pkg_4.circular_substring import circular_substring


class TestCircularSubstring(unittest.TestCase):
    __slots__ = ["_text", "_patterns"]

    def setUp(self):
        self._text = "circolare_circular"
        self._patterns = ["arci", "rcir", "larc", "rcirx", "circo", "ci", "lar", "_x", "x_"]

    def testNormalMatch(self):
        self.assertTrue(circular_substring(self._patterns[4], self._text))
        self.assertTrue(circular_substring(self._patterns[5], self._text))
        self.assertTrue(circular_substring(self._patterns[6], self._text))

    def testCircularMatch(self):
        self.assertTrue(circular_substring(self._patterns[0], self._text))
        self.assertTrue(circular_substring(self._patterns[1], self._text))
        self.assertTrue(circular_substring(self._patterns[2], self._text))

    def testNoMatch(self):
        self.assertFalse(circular_substring(self._patterns[3], self._text))
        self.assertFalse(circular_substring(self._patterns[7], self._text))
        self.assertFalse(circular_substring(self._patterns[8], self._text))
