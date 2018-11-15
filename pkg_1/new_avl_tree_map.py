from TdP_collections.map.binary_search_tree import TreeMap


class NewAVLTreeMap(TreeMap):
    # -------------------------- nested _Node class --------------------------
    class _Node(TreeMap._Node):
        __slots__ = '_balance_factor'  # additional data member to store height

        def __init__(self, element, parent=None, left=None, right=None):
            super().__init__(element, parent, left, right)
            self._balance_factor = 0

        def get_balance_factor(self):
            return self._balance_factor

        def set_balance_factor(self, bf):
            self._balance_factor = bf

    # ------------------------- positional-based utility methods -------------------------
    def _recompute_balance_factor(self, p):
        if not self._isbalanced(p):
            self._rebalance(p)
            return
        par = self.parent(p)
        if par is not None:
            if self.left(par) == p:
                par._node._balance_factor += 1
            elif self.right(par) == p:
                par._node._balance_factor -= 1
            if par._node._balance_factor != 0:
                self._recompute_balance_factor(par)

    def _isbalanced(self, p):
        """ ok """
        return abs(p._node.get_balance_factor()) <= 1

    def _tall_child(self, p, favorleft=False):
        pass

    def _tall_grandchild(self, p):
        pass

    def _rebalance(self, p):
        if p._node.get_balance_factor < 0:
            if p._node._r

    # ---------------------------- override balancing hooks ----------------------------
    def _rebalance_insert(self, p):
        self._rebalance(p)

    def _rebalance_delete(self, p):
        self._rebalance(p)
