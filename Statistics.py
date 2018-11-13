from TdP_collections.map.avl_tree import AVLTreeMap


class Statistics:

    __slots__ = ['__map', '__tot_occurrences']

    def __init__(self):
        self.__map = AVLTreeMap()

    def add(self, k, v):
        pass

    def occurrences(self):
        return self.__tot_occurrences

    def average(self):
        pass

    def median(self):
        pass

    def percentile(self, j=20):
        pass

    def most_frequent(self, j):
        pass




    def __len__(self):
        pass
