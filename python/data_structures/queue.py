from data_structures.invalid_operation_error import InvalidOperationError

class Queue:

    # The constructor initializes the queue.

    def __init__(self):
        # The front pointer points to the first node in the queue.
        self.front = None
        # The rear pointer points to the last node in the queue.
        self.rear = None

    # The enqueue method adds a new node to the queue.

    def enqueue(self, value):
        # Create a new node with the given value.
        new_node = Node(value)
        # If the queue is empty, set the front and rear pointers to the new node.
        if self.front is None:
            self.front = new_node
            self.rear = new_node
        # Otherwise, set the next pointer of the rear node to the new node, and then set the rear pointer to the new node.
        else:
            self.rear.next = new_node
            self.rear = new_node

    # The dequeue method removes the first node from the queue.

    def dequeue(self):
        # If the queue is empty, raise an exception.
        if self.front is None:
            raise InvalidOperationError("Queue is empty")
        # Save the value of the first node.
        value = self.front.value
        # Set the front pointer to the next node.
        self.front = self.front.next
        # If the front pointer is now None, set the rear pointer to None as well.
        if self.front is None:
            self.rear = None
        return value

    # The peek method returns the value of the first node in the queue, without removing it.

    def peek(self):
        # If the queue is empty, raise an exception.
        if self.front is None:
            raise InvalidOperationError("Queue is empty")
        return self.front.value

    # The is_empty method returns True if the queue is empty, and False otherwise.

    def is_empty(self):
        return self.front is None


class Node:

    # The constructor initializes a node with the given value.

    def __init__(self, value):
        self.value = value
        self.next = None