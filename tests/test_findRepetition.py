from pkg_3.find_copy import find_repetition
import unittest


class TestFindRepetition(unittest.TestCase):

    __slots__ = ["_testCases"]

    def setUp(self):
        self._testCases = []

    def testFindRepetition_trueResults(self):
        expected = []  # expected tests result

        self._testCases.append('./copy/test_copy_1')
        expected.append([['./copy/test_copy_1/copyDir.py', './copy/test_copy_1/copyDir2.py']])
        self._testCases.append('./copy/test_copy_2')
        expected.append([])

        for i in range(len(self._testCases)):
            self.assertEqual(expected[i], find_repetition(self._testCases[i]))


    def testFindRepetition_falseResults(self):
        expected = []  # expected tests result

        self._testCases.append('./copy/test_copy_3')
        expected.append()
        self._testCases.append('./copy/test_copy_4')
        expected.append()

        for i in range(len(self._testCases)):
            self.assertEqual(expected[i],find_repetition(self._testCases[i]))