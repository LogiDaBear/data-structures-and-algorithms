from data_structures.binary_tree import BinaryTree
from data_structures.hashtable import HashTable



from hashtable import Hashtable

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def traverse_tree(root, values_set):
    if root:
        traverse_tree(root.left, values_set)
        values_set.add(root.val)
        traverse_tree(root.right, values_set)

def tree_intersection(tree1, tree2):
    # Hashtable to store values from tree1
    value_map = Hashtable()

    # List to store values from tree2
    tree2_values = set()

    # Traverse tree1 and add values to the Hashtable
    def add_to_hashtable(root):
        if root:
            value_map.set(root.val, True)
            add_to_hashtable(root.left)
            add_to_hashtable(root.right)

    add_to_hashtable(tree1)

    # Traverse tree2 and add values to the list
    traverse_tree(tree2, tree2_values)

    # Initialize an empty set to store common values
    common_values = set()

    # Check if each value in tree2 exists in the Hashtable
    for val in tree2_values:
        if value_map.has(val):
            common_values.add(val)

    # Return the set of common values
    return common_values