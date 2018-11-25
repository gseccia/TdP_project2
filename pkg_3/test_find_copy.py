from pkg_3.find_copy import find_repetition
import unittest


class TestFindRepetition(unittest.TestCase):

    __slots__ = ["_directories"]  # lista delle cartelle di test

    def setUp(self):
        self._directories = ['./copy/test_copy_1', './copy/test_copy_2', './copy/test_copy_3', './copy/test_copy_4']

    def testFindRepetition_trueResults(self):
        expected_lists = [
            [['%s/copyDir.py' % self._directories[0], '%s/copyDir2.py' % self._directories[0]]],
            [
                ['%s/test1' % self._directories[1], '%s/test1_2' % self._directories[1]],
                ['%s/test2' % self._directories[1], '%s/test2_2' % self._directories[1]],
            ]
        ]  # lista di liste di collisioni attese sulle directory 1 e 2
        for i in range(0, 2):
            self.assertEqual(expected_lists[i], find_repetition(self._directories[i]))

    def testFindRepetition_falseResults(self):
        expected_lists = []  # lista di liste di duplicati per file attese nelle cartelle 3 e 4. E' vuota
        for i in range(2, 4):
            lists = find_repetition(self._directories[i])
            self.assertEqual(expected_lists, lists)
