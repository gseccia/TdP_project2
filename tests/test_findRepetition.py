from pkg_3.find_copy import find_repetition
import unittest


class TestFindRepetition(unittest.TestCase):

    __slots__ = ["_testCases"]

    def setUp(self):
        self._testCases = []

    def testFindRepetition_trueResults(self):
        self._testCases.append('./copy/test_copy_1')
        self._testCases.append('./copy/test_copy_2')

        for path in self._testCases:
            self.assertTrue(find_repetition(path))

    def testFindRepetition_falseResults(self):
        self._testCases.append('./copy/test_copy_3')
        self._testCases.append('./copy/test_copy_4')

        for path in self._testCases:
            self.assertFalse(find_repetition(path))