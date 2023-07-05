from data_structures.binary_tree import BinaryTree
from collections import deque


def breadth_first(tree):
    if tree.root is None:
        return []
    breadth = deque()
    breadth.append(tree.root)
    traversal = []

    while len(breadth) > 0:
        front = breadth.popleft()
        traversal.append(front.value)

        if front.left is not None:
            breadth.append(front.left)

        if front.right is not None:
            breadth.append(front.right)

    return traversal
