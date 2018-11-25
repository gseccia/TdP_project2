import random
import time

from pkg_1.new_avl_tree_map import NewAVLTreeMap


# verifichiamo che il bilanciamento del nodo sia coerente con la differenza di altezza dei suoi sottoalberi
def validate_balance_factor(tree, do_print=False):
    counter = 0

    for elem in tree.inorder():
        left_child = tree.left(elem)
        right_child = tree.right(elem)
        if left_child is None:
            left_height = 0
        else:
            left_height = tree.height(left_child) + 1

        if right_child is None:
            right_height = 0
        else:
            right_height = tree.height(right_child) + 1

        checked_balance_factor = left_height - right_height

        if elem._node._balance_factor == checked_balance_factor and abs(elem._node._balance_factor) < 2:
            counter += 1

        if do_print:
            print("Il nodo {} ha balance_factor: {:<3}".format(elem.key(), elem._node._balance_factor))

    return counter


# calcoliamo il numero di nodi presenti nel new_avl_tree
def count_element_in_tree(tree):
    counter = 0
    for elem in tree.inorder():
        counter += 1
    return counter


def print_balance(tree):
    for elem in tree.inorder():
        print("Il fattore di bilanciamento di {} è {}".format(elem.key(), elem._node._balance_factor))


def test_avl_tree(repetition=1):
    tree = NewAVLTreeMap()
    success = 0

    print("----- Verranno prodotti {} NewAvlTree di Test -----".format(repetition))
    time.sleep(3)

    for i in range(repetition):
        print("\n-------------------- NEW AVL TREE {} --------------------\n".format(i+1))
        list = random.sample(range(20), random.randint(1, 20))

        print("---------- INSERT ----------")
        for i in range(len(list)):
            tree[list[i]] = list[i]
            if validate_balance_factor(tree) == count_element_in_tree(tree):
                print("Inserisco elemento: {:<3} -> OK".format(list[i]))
            else:
                print("Inserisco elemento: {:<3} -> NO".format(list[i]))

        if validate_balance_factor(tree) == count_element_in_tree(tree):
            print("\n--> Tutti gli elementi sono stati correttamente inseriti nella struttura\n")

        print("---------- NEW AVL TREE AFTER INSERT ----------\n")
        print(tree.root()._node)
        do_print = True
        validate_balance_factor(tree, do_print)

        number_of_delete = random.randint(1, len(list))

        print("\n---------- DELETE ----------")
        for i in range(number_of_delete):
            index = random.randint(0, len(list) - 1)
            to_deleted = list[index]
            del tree[to_deleted]
            if validate_balance_factor(tree) == count_element_in_tree(tree):
                print("Cancello nodo con chiave: {:<3} -> OK".format(list[index]))
            else:
                print("Cancello nodo con chiave: {:<3} -> NO".format(list[index]))
            del list[index]

        if count_element_in_tree(tree) > 0:
            if validate_balance_factor(tree) == count_element_in_tree(tree):
                success += 1

            print("\n--> Tutte le cancellazioni sono state effetuate correttamente\n")

            print("---------- NEW AVL TREE AFTER DELETE ----------\n")
            print(tree.root()._node)
            do_print = True
            validate_balance_factor(tree, do_print)

        if tree.is_empty():
            success += 1

    print("\n-------------------------------------------------------------------------------------------")
    print("Il numero di alberi creati è: ", repetition)
    print("Il numero di NewAvlTree dopo operazioni casuali di inserimento e cancellazione sono: ",success)
    print("La percentuale di successo è: {}%".format((success / repetition) * 100))
    print("-------------------------------------------------------------------------------------------\n")

test_avl_tree(100)
