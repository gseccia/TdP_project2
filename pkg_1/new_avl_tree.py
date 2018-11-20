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
    def _recompute_balance_factor(self):
        pass

    def _isbalanced(self, p):
        """ ok """
        return abs(p._node.get_balance_factor()) <= 1

    def _tall_child(self, p, favorleft=False):
        pass

    def _tall_grandchild(self, p):
        pass

    def _rebalance(self, p):
        pass

    # ---------------------------- override balancing hooks ----------------------------
    def _rebalance_insert(self, p):

        # self._rebalance(p)

        if p.key() is self.root().key():
            return

        parent = self.parent(p)
        #
        # print("Il padre è {}".format(parent.value()))
        # print("Il fattore di bilanciamento del padre è {}\n".format(parent._node.get_balance_factor()))

        if self.left(parent) is not None and self.left(parent).key() == p.key():
            parent._node.set_balance_factor(parent._node.get_balance_factor() + 1)
        else:
            parent._node.set_balance_factor(parent._node.get_balance_factor() - 1)

        if abs(parent._node.get_balance_factor()) == 2:
            print("RESTRUCTURE\n")
            self._our_restructure(parent)
            parent = self.parent(parent)

        if parent._node.get_balance_factor() != 0:
            self._rebalance_insert(parent)

    def print_bilanciamento(self):
        for elem in self.inorder():
            print("Il fattore di bilanciamento di {} è {}".format(elem.key(), elem._node.get_balance_factor()))

    def _rebalance_delete(self, p):
        # self._rebalance(p)
        print(" rebalance delete")

        if p is None:
            return

        parent = p

        print("Il padre è {}".format(parent.key()))
        print("Il fattore di bilanciamento del padre è {}\n".format(parent._node.get_balance_factor()))

        if self.left(parent) is None and self.right(parent) is None:
            parent._node.set_balance_factor(0)
        elif self.left(parent) is not None:
            parent._node.set_balance_factor(parent._node.get_balance_factor() + 1)
        else:
            parent._node.set_balance_factor(parent._node.get_balance_factor() - 1)

        print("Dopo aver eliminato, il fattore di bilanciamento di {} è {}\n".format(parent.key(),
                                                                                     parent._node.get_balance_factor()))

        if not self._isbalanced(parent):
            print("RESTRUCTURE\n")
            self._our_restructure(parent, True)
            parent = self.parent(parent)
            print("Il nodo da cui riparto per fare la our rebalance delete è: ",parent.key())

        if parent._node.get_balance_factor() == 0:
            self._our_rebalance_delete(parent)


    def _our_rebalance_delete(self, p, balanced=False):
        print("Our rebalance delete")
        # self._rebalance(p)

        if p.key() is self.root().key():
            return

        parent = self.parent(p)

        if self.left(parent) is not None and self.left(parent).key() == p.key():
            parent._node.set_balance_factor(parent._node.get_balance_factor() - 1)
        else:
            parent._node.set_balance_factor(parent._node.get_balance_factor() + 1)

        print("Dopo aver eliminato, il fattore di bilanciamento di {} è {}\n".format(parent.key(),
                                                                                     parent._node.get_balance_factor()))

        # Il fattore balanced mi dice se ho già bilaniato e quindi posso rientrare nel caso di _rebalance_insert
        # Appena bilancio il fattore balanced diventa true
        if not self._isbalanced(parent):
            print("RESTRUCTURE\n")

            if not balanced:
                balanced = True
            else:
                balanced = False

            # Il primo ribilanciamento che faccio proviene da una cancellazione, dato che balanced is False
            self._our_restructure(parent, balanced)
            parent = self.parent(parent)

        if parent._node.get_balance_factor() == 0:
            self._our_rebalance_delete(parent, balanced)

    def _isbalanced(self, p):
        return abs(p._node.get_balance_factor()) != 2


    def _our_restructure(self, p,remove = False):
        # Caso bilanciamento semplice (con una sola rotazione)

        # Prendi la y (z è p)
        z = p
        print("z", z.key())
        if z._node.get_balance_factor() < 0:  # b=-2 quindi prendi il figlio destro
            y = self.right(z)

        else:
            y = self.left(z)
        print("y", y.key())
        # Prendi la x
        if y._node.get_balance_factor() <= 0:
            x = self.right(y)
        else:
            x = self.left(y)
        print("x", x.key())
        # Trova a,b,c
        maxim_value = max(x.key(), y.key(), z.key())
        minim_value = min(x.key(), y.key(), z.key())
        c = self.find_position(maxim_value)
        print("c:", c.key())
        for elem in (x.key(), y.key(), z.key()):
            if elem not in (minim_value, maxim_value):
                b = self.find_position(elem)
                break

        print("b: ", b.key())
        a = self.find_position(minim_value)
        print("a: ", a.key())

        # Ristruttura caso base
        if self.is_leaf(x):
            if x.key() == a.key():
                if b._node.get_balance_factor() == 0: #b ha figlio destro da dare a c
                    c._node.set_balance_factor(1)
                    b._node.set_balance_factor(-1)
                    a._node.set_balance_factor(0)
                else:
                    c._node.set_balance_factor(0)
                    b._node.set_balance_factor(0)
                    a._node.set_balance_factor(0)

            elif x.key() == c.key():
                if b._node.get_balance_factor() == 0:  # b ha figlio sinistro da dare a c
                    c._node.set_balance_factor(0)
                    b._node.set_balance_factor(1)
                    a._node.set_balance_factor(-1)
                else:
                    c._node.set_balance_factor(0)
                    b._node.set_balance_factor(0)
                    a._node.set_balance_factor(0)

            self._restructure(x)
            print("ho terminato la restructure di un caso base")
            self.print_bilanciamento()
            return


        # Aggiorna i fattori di bilanciamento
        elif x.key() == a.key():

            # b._node.set_balance_factor(abs(b._node.get_balance_factor()-1))
            if b._node.get_balance_factor() == 0:
                b._node.set_balance_factor(-1)
                c._node.set_balance_factor(1)

            else:
                b._node.set_balance_factor(0)
                c._node.set_balance_factor(0)


        elif x.key() == c.key():

            # Settiamo il bilanciamento di c
            if b._node.get_balance_factor() == 0:  # Se il bilanciamento di b era uguale a 0:
                a._node.set_balance_factor(-1)  #
                b._node.set_balance_factor(1)
            else:
                a._node.set_balance_factor(0)
                b._node.set_balance_factor(0)



        elif x.key() == b.key() and z.key() == a.key():
            print("Caso 3 e 4")
            print(b._node.get_balance_factor())
            print(b.key())


            # c._node.set_balance_factor(-1)
            # b._node.set_balance_factor(0)
            # a._node.set_balance_factor(0)

            #b avrà tutti e due i sottoalberi
            if b._node.get_balance_factor() == 0:
                a._node.set_balance_factor(0)
                c._node.set_balance_factor(0)

            elif b._node.get_balance_factor() == -1:
                a._node.set_balance_factor(1)
                c._node.set_balance_factor(0)

            elif b._node.get_balance_factor() == 1:
                a._node.set_balance_factor(0)
                c._node.set_balance_factor(-1)

            b._node.set_balance_factor(0)

        elif x.key() == b.key() and z.key() == a.key():
            print("Caso 3 e 4")
            print(b._node.get_balance_factor())
            print(b.key())

            # c._node.set_balance_factor(-1)
            # b._node.set_balance_factor(0)
            # a._node.set_balance_factor(0)

            # b avrà tutti e due i sottoalberi
            if b._node.get_balance_factor() == 0:
                a._node.set_balance_factor(0)
                c._node.set_balance_factor(0)

            elif b._node.get_balance_factor() == -1:
                a._node.set_balance_factor(1)
                c._node.set_balance_factor(0)

            elif b._node.get_balance_factor() == 1:
                a._node.set_balance_factor(0)
                c._node.set_balance_factor(-1)

            b._node.set_balance_factor(0)

        self._restructure(x)









