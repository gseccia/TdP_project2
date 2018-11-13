from TdP_collections.map.avl_tree import AVLTreeMap
from TdP_collections.map.binary_search_tree import TreeMap


class NewAVLTreeMap(AVLTreeMap):
    # -------------------------- nested _Node class --------------------------
    class _Node(TreeMap._Node):
        """Node class for AVL maintains height value for balancing.

        We use convention that a "None" child has height 0, thus a leaf has height 1.
        """
        __slots__ = '_balance_factor'  # additional data member to store height

        def __init__(self, element, parent=None, left=None, right=None):
            super().__init__(element, parent, left, right)

        def left_height(self):
            pass

        def right_height(self):
            pass
    # ------------------------- positional-based utility methods -------------------------

    def _recompute_height(self, p):
        super()._recompute_height(p)

    def _isbalanced(self, p):
        return super()._isbalanced(p)

    def _tall_child(self, p, favorleft=False):
        return super()._tall_child(p, favorleft)

    def _tall_grandchild(self, p):
        return super()._tall_grandchild(p)

    def _rebalance(self, p):
        super()._rebalance(p)

    def _rebalance_insert(self, p):
        super()._rebalance_insert(p)

    def _rebalance_delete(self, p):
        super()._rebalance_delete(p)