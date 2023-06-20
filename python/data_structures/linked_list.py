class Node:
    def __init__(self, value, _next=None):
        self.value = value
        self.next = _next


class LinkedList:
    def __init__(self, head=None, values=None, insert=None):
        self.head = None

    def insert(self, value):
        node = Node(value)
        if self.head:
            node.next = self.head
        self.head = node


    # ChatGPT'd append method
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def __str__(self):
        if self.head == None:
            return "NULL"
        else:
            current = self.head
            output = ""
            while current:
                output += f"{{ {current.value} }} -> "
                current = current.next
            output += "NULL"
            return output

    # def includes(self, value):
    #     current = self.head
    #     while current:
    #         if current.value == value:
    #             return True
    #         current = current.next
    #     return False
    class TargetError:
        pass