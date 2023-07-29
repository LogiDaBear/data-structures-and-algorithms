import pytest
from code_challenges.tree_intersection import tree_intersection
from data_structures.binary_tree import BinaryTree, Node
from data_structures.queue import Queue


def test_exists():
    assert tree_intersection


# @pytest.mark.skip("TODO")
def test_tree_intersection():

    tree_a = BinaryTree()
    values = [150, 100, 250, 75, 160, 200, 350, 125, 175, 300, 500]
    add_values_to_empty_tree(tree_a, values)

    tree_b = BinaryTree()
    values = [42, 100, 100, 15, 160, 200, 350, 125, 175, 4, 500]
    add_values_to_empty_tree(tree_b, values)

    actual = tree_intersection(tree_a, tree_b)
    expected = [125, 175, 100, 160, 500, 200, 350]

    assert sorted(actual) == sorted(expected)


def add_values_to_empty_tree(tree, values):
    """
    Helper function to add given values to BinaryTree
    """
    tree.root = Node(values.pop())
    q = Queue()

    q.enqueue(tree.root)

    while values:
        node = q.dequeue()
        node.left = Node(values.pop())
        node.right = Node(values.pop()) if values else None
        q.enqueue(node.left)
        q.enqueue(node.right)
def test_traverse_a():
    tree_a = BinaryTree()
    values = [150, 100, 250, 75, 160, 200, 350, 125, 175, 300, 500]
    add_values_to_empty_tree(tree_a, values)
    hashmap = {}
    def traverse_a(node):
        if node:
            hashmap[node.value] = node.value
            traverse_a(node.left)
            traverse_a(node.right)
    traverse_a(tree_a.root)
    actual = hashmap
    expected = {150: 150, 100: 100, 250: 250, 75: 75, 160: 160, 200: 200, 350: 350, 125: 125, 175: 175, 300: 300, 500: 500}
    assert actual == expected

def test_traverse_b():
    tree_b = BinaryTree()
    values = [42, 100, 100, 15, 160, 200, 350, 125, 175, 4, 500]
    add_values_to_empty_tree(tree_b, values)
    hashmap = {}
    def traverse_b(node):
        if node:
            hashmap[node.value] = node.value
            traverse_b(node.left)
            traverse_b(node.right)
    traverse_b(tree_b.root)
    actual = hashmap
    expected = {42: 42, 100: 100, 15: 15, 160: 160, 200: 200, 350: 350, 125: 125, 175: 175, 4: 4, 500: 500}
    assert actual == expected