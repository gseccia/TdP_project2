import unittest
from pkg_2.statistics import Statistics


class TestStatistics(unittest.TestCase):
    __slots__ = ["_s", "_expected_stat"]

    def setUp(self):
        self._s = Statistics("./dataset.csv")
        self._expected_stat = [(1, 1, 30), (2, 2, 40), (3, 3, 60), (4, 1, 20), (5, 1, 20),
                               (6, 1, 20)]  # (key,frequency,total) attesi

    def test_add(self):
        for i in range(0, 6):
            self.assertEqual(self._s._map[str(i + 1)]._occurrence, self._expected_stat[i][1])
            self.assertEqual(self._s._map[str(i + 1)]._total, self._expected_stat[i][2])

    def test_occurrences(self):
        expected = 9
        self.assertEqual(expected, self._s.occurrences())

    def test_average(self):
        sum = 0
        for i in range(1, 7):
            sum += self._s._map[str(i)]._total
        average = sum / self._s.occurrences()
        self.assertEqual(average, self._s.average())

    def test_percentile(self, j=20):
        sequence = []
        for key in self._s._map:
            sequence += [key] * self._s._map[key]._occurrence
        index = j * (len(sequence) + 1) // 100
        result = sequence[index]
        self.assertEqual(result, self._s.percentile(j))

    def test_median(self):
        self.test_percentile(50)

    def test_mostfrequent(self, j=3):
        self._expected_stat.sort(key=lambda elem: elem[1], reverse=True)
        k = 0
        for key in self._s.most_frequent(j):
            self.assertEqual(str(self._expected_stat[k][0]), key)
            k += 1


if __name__ == '__main__':
    unittest.main(verbosity=True, buffer=True)
