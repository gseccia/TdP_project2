from TdP_collections.map.avl_tree import AVLTreeMap
from pkg_1.new_avl_tree import NewAVLTreeMap
from operator import itemgetter


class Statistics:
    class _Stat:
        __slots__ = ['_occurrence', '_total']

        def __init__(self, o, v):
            self._occurrence = o
            self._total = v

        def get_occurrence(self):
            return self._occurrence

        def get_total(self):
            return self._total

    __slots__ = ['_map', '_tot_occurrences']

    def __init__(self):
        self._map = NewAVLTreeMap()
        self._tot_occurrences = 0

    def add(self, k, v):
        self._tot_occurrences += 1
        if k in self._map:
            old = self._map[k]
            self._map[k] = self._Stat(old.get_occurrence() + 1, old.get_total() + v)
        else:
            self._map[k] = self._Stat(1, v)

    def occurrences(self):
        return self._tot_occurrences

    def average(self):
        av = 0
        for stat in self._map:
            av += self._map[stat].get_total() / self._map[stat].get_occurrence()
        return av / len(self._map)

    def median(self):
        return self.percentile(50)

    def percentile(self, j=20):
        per = 0
        for elem in self._map:
            per += self._map[elem].get_occurrence() / self._tot_occurrences * 100
            if per >= j:
                return elem

    def most_frequent(self, j=1):
        bucket = list()
        for key in self._map:
            bucket.append([self._map[key].get_occurrence(), key])
        bucket = sorted(bucket, reverse=True, key=itemgetter(0))
        most = list()
        for i in range(j):
            most.append(bucket[i][1])
        return most


s = Statistics()
print(s.occurrences())
s.add(1, 30)
print(s.occurrences())
s.add(2, 20)
print(s.occurrences())
s.add(2, 20)
print(s.occurrences())

s.add(3, 20)
s.add(3, 20)
s.add(3, 20)
s.add(4, 20)
s.add(5, 20)
s.add(6, 20)
print(s.occurrences())
print(s.average())
print(s.median())

print("most frequent")
print(s.most_frequent(2))
print(s._map.root()._node)
