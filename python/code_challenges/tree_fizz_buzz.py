from data_structures.binary_tree import BinaryTree
from data_structures.kary_tree import KaryTree, Node


class TreeNode:
    def __init__(self, value=None):
        self.value = value
        self.children = []

def fizz_buzz_tree(tree):
    if not tree.root:
        return None

    new_tree = KaryTree(TreeNode(None))  # Create a new KaryTree with the modified TreeNode
    process_node(tree.root, new_tree.root)  # Pass the root nodes to process

    return new_tree

def process_node(current_node, new_node):
    if current_node.value % 3 == 0 and current_node.value % 5 == 0:
        new_node.value = "FizzBuzz"
    elif current_node.value % 3 == 0:
        new_node.value = "Fizz"
    elif current_node.value % 5 == 0:
        new_node.value = "Buzz"
    else:
        new_node.value = str(current_node.value)

    for child_node in current_node.children:
        new_child_node = TreeNode(None)
        new_node.children.append(new_child_node)
        process_node(child_node, new_child_node)
