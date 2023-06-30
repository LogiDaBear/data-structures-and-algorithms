from data_structures.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
 

    def add(self, value):
        if not self.root: # ALWAYS check for self.root
            self.root = Node(value)
            return
        def walk(root, new_node):
            if not root:
                return
            if new_node.value < root.value:
                if root.left:
                    walk(root.left, new_node)
                else:
                    root.left = new_node
            else:
                if root.right:
                    walk(root.right, new_node)
                else:
                    root.right = new_node
        new_node = Node(value)
        walk(self.root, new_node)
        
    def contains(self, value):
        def walk(root, value):
            if not root:
                return False
            if root.value == value:
                return True
            if value < root.value:
                return walk(root.left, value)
            else:
                return walk(root.right, value)

        return walk(self.root, value)
