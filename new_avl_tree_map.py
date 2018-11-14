from TdP_collections.map.binary_search_tree import TreeMap


class NewAVLTreeMap(TreeMap):
    # -------------------------- nested _Node class --------------------------
    class _Node(TreeMap._Node):
        """Node class for AVL maintains height value for balancing.

        We use convention that a "None" child has height 0, thus a leaf has height 1.
        """
        __slots__ = '_balance_factor'  # additional data member to store height

        def __init__(self, element, parent=None, left=None, right=None):
            super().__init__(element, parent, left, right)
            self._balance_factor = 0

        def left_height(self):
            pass

        def right_height(self):
            pass

    # ------------------------- positional-based utility methods -------------------------

    def _recompute_height(self, p):
        pass

    def _isbalanced(self, p):
        pass

    def _tall_child(self, p, favorleft=False):
        pass

    def _tall_grandchild(self, p):
        pass

    def _rebalance(self, p):
        pass

    def _rebalance_insert(self, p):
        pass

    def _rebalance_delete(self, p):
        pass
