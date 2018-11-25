from TdP_collections.map.binary_search_tree import TreeMap


class NewAVLTreeMap(TreeMap):
    # -------------------------- nested _Node class --------------------------
    class _Node(TreeMap._Node):
        __slots__ = '_balance_factor'  # additional data member to store height

        def __init__(self, element, parent=None, left=None, right=None):
            super().__init__(element, parent, left, right)
            self._balance_factor = 0

        def __str__(self, level=0):
            ret = "\t" * level + repr(self._element._key) + "\n"
            if self._left is not None:
                ret += self._left.__str__(level + 1)
            if self._right is not None:
                ret += self._right.__str__(level + 1)
            return ret

        def __repr__(self):
            return '<tree node representation>'

    # ------------------------- positional-based utility methods -------------------------
    def _recompute_balance_factor(self, p):
        z = p
        if z._node._balance_factor <= 0:  # b=-2 quindi prendi il figlio destro
            y = self.right(z)
        else:
            y = self.left(z)

        if y._node._balance_factor < 0:
            x = self.right(y)
        else:
            x = self.left(y)

        abc_undefined = [x, y, z]
        abc_undefined.sort(key=lambda x: x.key())
        c = abc_undefined[2]
        a = abc_undefined[0]
        b = abc_undefined[1]

        # Ristruttura caso base
        if self.is_leaf(x):
            if x == a and b._node._balance_factor == 0:  # b ha figlio destro da dare a c
                c._node._balance_factor = 1
                b._node._balance_factor = -1
                a._node._balance_factor = 0
            elif x == c and b._node._balance_factor == 0:  # b ha figlio sinistro da dare a c
                c._node._balance_factor = 0
                b._node._balance_factor = 1
                a._node._balance_factor = -1
            elif x == b and z == a and c._node._balance_factor == 0:  # Qui era b ma ho messo c
                b._node._balance_factor = -1
                a._node._balance_factor = 0
                c._node._balance_factor = -1
            else:
                b._node._balance_factor = 0
                a._node._balance_factor = 0
                c._node._balance_factor = 0
        # Aggiorna i fattori di bilanciamento
        elif x == a:
            # Caso1 1
            if b._node._balance_factor == 0:
                b._node._balance_factor = -1
                c._node._balance_factor = 1
            else:
                b._node._balance_factor = 0
                c._node._balance_factor = 0
        elif x == c:
            # Caso 2
            # Settiamo il bilanciamento di c
            if b._node._balance_factor == 0:  # Se il bilanciamento di b era uguale a 0:
                a._node._balance_factor = -1  #
                b._node._balance_factor = 1
            else:
                a._node._balance_factor = 0
                b._node._balance_factor = 0
        elif x == b and z == a:
            # Caso 3
            # b avrà tutti e due i sottoalberi
            if b._node._balance_factor == 0:
                a._node._balance_factor = 0
                c._node._balance_factor -= 1
                b._node._balance_factor = c._node._balance_factor
            elif b._node._balance_factor == -1:
                a._node._balance_factor = 1
                c._node._balance_factor -= 1
                b._node._balance_factor = c._node._balance_factor
            elif b._node._balance_factor == 1:
                if c._node._balance_factor == 0:
                    #Caso doppia ristrutturazione
                    self._restructure(x)
                    a._node._balance_factor = 0
                    c._node._balance_factor = 0
                    b._node._balance_factor = self._recompute_balance_factor(c) \
                        ._node._balance_factor  # c._node._balance_factor
                    return b
                else:
                    b._node._balance_factor = 0
                    a._node._balance_factor = 0
                    c._node._balance_factor = -1
        elif x == b and z == c:
            # Caso 4
            # b avrà tutti e due i sottoalberi
            if b._node._balance_factor == 0:
                c._node._balance_factor = 0
                a._node._balance_factor += 1
                b._node._balance_factor = a._node._balance_factor
            elif b._node._balance_factor == 1:
                c._node._balance_factor = -1
                a._node._balance_factor += 1
                b._node._balance_factor = a._node._balance_factor
            else:
                c._node._balance_factor = 0
                a._node._balance_factor = 1
                b._node._balance_factor = 0

        return self._restructure(x)

    def _isbalanced(self, p):
        """ ok """
        return abs(p._node._balance_factor) <= 1

    # ---------------------------- override balancing hooks ----------------------------
    def _rebalance_insert(self, p):

        if p.key() is self.root().key():
            return

        parent = self.parent(p)

        if self.left(parent) is not None and self.left(parent) == p:
            parent._node._balance_factor += 1
        else:
            parent._node._balance_factor -= 1

        if abs(parent._node._balance_factor) == 2:
            self._recompute_balance_factor(parent)
            parent = self.parent(parent)

        if parent._node._balance_factor != 0:
            self._rebalance_insert(parent)

    def _rebalance_delete(self, parent):
        if parent is None:
            return

        if self.is_leaf(parent):
            parent._node._balance_factor = 0
        elif self.num_children(
                parent) == 2:  # Se è stato eliminato un nodo interno e il padre ha ancora tutti e due i figli
            if self.is_leaf(self.left(parent)) and self.is_leaf(self.right(parent)):
                parent._node._balance_factor = 0
            elif self.is_leaf(self.left(parent)):
                parent._node._balance_factor -= 1
            elif self.is_leaf(self.right(parent)):
                parent._node._balance_factor += 1
        elif self.left(parent) is not None:
            parent._node._balance_factor += 1
        else:
            parent._node._balance_factor -= 1

        if not self._isbalanced(parent):
            parent = self._recompute_balance_factor(parent)

        if parent._node._balance_factor == 0:
            self._rebalance_delete_parent(parent)

    def _rebalance_delete_parent(self, p):
        if p == self.root():
            return

        parent = self.parent(p)

        if self.left(parent) is not None and self.left(parent) == p:
            parent._node._balance_factor -= 1
        else:
            parent._node._balance_factor += 1

        if not self._isbalanced(parent):
            self._recompute_balance_factor(parent)
            parent = self.parent(parent)

        if parent._node._balance_factor == 0:
            self._rebalance_delete_parent(parent)
