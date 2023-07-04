#Rogers starter code:
class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, root=None):
        self.root = root


    def pre_order(self, values=[]):
        def walk(input_node, value_list):
            if not input_node:
                return
            value_list.append(input_node.value)
            walk(input_node.left, value_list)
            walk(input_node.right, value_list)

        walk(self.root, values)
        return values

    def in_order(self, values=[]):
        def walk(input_node, value_list):
            if not input_node:
                return
            walk(input_node.left, value_list)
            value_list.append(input_node.value)
            walk(input_node.right, value_list)

        walk(self.root, values)
        return values

    def post_order(self, values=[]):
        def walk(input_node, value_list):
            if not input_node:
                return
            walk(input_node.left, value_list)
            walk(input_node.right, value_list)
            value_list.append(input_node.value)

        walk(self.root, values)
        return values
    
    #tree-max
    def find_maximum_value(self):
        if self.root is None:
            raise Exception("Tree is empty.")

        return self._find_maximum_value_recursive(self.root)
    
    #Chatgpt helper function
    def _find_maximum_value_recursive(self, node):
        if node is None:
            return float('-inf')

        max_value = node.value
        left_max = self._find_maximum_value_recursive(node.left)
        right_max = self._find_maximum_value_recursive(node.right)

        if left_max > max_value:
            max_value = left_max
        if right_max > max_value:
            max_value = right_max

        return max_value