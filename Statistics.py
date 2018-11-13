from TdP_collections.map.avl_tree import AVLTreeMap


class Statistics:
    class _Stat:
        __slots__ = ['_occurrence', '_total']

        def __init__(self, o, v):
            self._occurrence = o
            self._total = v

        def _increment(self, v):
            self._occurrence += 1
            self._total += v

        def get_occurrence(self):
            return self._occurrence

        def get_total(self):
            return self._total

    __slots__ = ['_map', '_tot_occurrences']

    def __init__(self):
        self._map = AVLTreeMap()
        self._tot_occurrences = 0

    def add(self, k, v):
        self._tot_occurrences += 1
        try:
            old = self._map[k]
            self._map[k] = self._Stat(old.get_occurrence(), old.get_total())
        except KeyError:
            self._map[k] = self._Stat(1, v)

    def occurrences(self):
        return self._tot_occurrences

    def average(self):
        av = 0
        for stat in self._map:
            av += self._map[stat].get_total() / self._tot_occurrences * self._map[stat].get_occurrence()
        return av

    def median(self):
        return self.percentile(50)

    def percentile(self, j=20):
        per = 0
        for elem in self._map:
            per += self._map[elem].get_occurrence() / self._tot_occurrences * 100
            if per >= j:
                return self._map[elem].get_total() / self._map[elem].get_occurrence()

    def most_frequent(self, j):
        pass


s = Statistics()
print(s.occurrences())

s.add(1,20)
print(s.occurrences())
s.add(2,29)
print(s.occurrences())

s.add(3,27)
s.add(3,27)
s.add(3,27)
print(s.average())
print(s.median())