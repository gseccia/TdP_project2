from pkg_1.new_avl_tree_map import NewAVLTreeMap
from operator import itemgetter
import csv

class Statistics:
    class _Stat:
        __slots__ = ['_occurrence', '_total']

        def __init__(self, v):
            self._occurrence = 1
            self._total = v

        def increment_stat(self, v):
            self._occurrence += 1
            self._total += v

    __slots__ = ['_map', '_tot_occurrences', '_total', '_key_type']

    def __init__(self, path_to_csv=None, key_type=int):
        self._map = NewAVLTreeMap()
        self._tot_occurrences = 0
        self._total = 0
        self._key_type = key_type

        if path_to_csv is not None:
            with open(path_to_csv, 'r') as filecsv:
                self._key_type = str
                reader = csv.reader(filecsv)
                for row in reader:
                    self.add(row[0], int(row[1]))

    def add(self, k, v):
        if self._key_type != type(k):
            raise TypeError("k is not a valid key")
        if type(v) != int:
            raise TypeError("v is not integer")
        self._tot_occurrences += 1
        self._total += v
        if k in self._map:
            self._map[k].increment_stat(v)
        else:
            self._map[k] = self._Stat(v)

    def occurrences(self):
        return self._tot_occurrences

    def average(self):
        return 0 if self._map.is_empty() else self._total / self._tot_occurrences

    def median(self):
        return self.percentile(50)

    def percentile(self, j=20):
        if j < 0 or j > 100:
            raise ValueError("j must be 0 < j < 100")
        per = 0
        for elem in self._map:
            per += self._map[elem]._occurrence / self._tot_occurrences * 100
            if per >= j:
                return elem

    def most_frequent(self, j=1):
        if j > self.len():
            raise ValueError("Too much element required")
        if j <= 0:
            raise ValueError("Negative or 0 value not admitted")
        bucket = list()
        for key in self._map:
            bucket.append([self._map[key]._occurrence, key])
        bucket = sorted(bucket, reverse=True, key=itemgetter(0))
        most = list()
        for i in range(j):
            most.append(bucket[i][1])
        return most

    def len(self):
        return len(self._map)
