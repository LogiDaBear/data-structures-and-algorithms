BLANK = object()

class Hashtable:
    """
    A class that represents a Hashtable, which implements a key-value store.
    Collisions are handled by using a simple form of separate chaining.
    """

    def __init__(self, size=1024):
        """
        Initializes an instance of a Hashtable.

        Args:
            size (int): The number of buckets in the hashtable.
        """
        self.size = size
        self.values = size * [BLANK]
        self.pairs = size * [(None, None)]
        self._buckets = [[["silent", True], ["listen", "to me"]], [["ahmad", 30]]]

    def hash(self, key):
        """
        Calculates the hash value of the key.

        Args:
            key (str): The key to be hashed.

        Returns:
            int: The hash value.
        """
        total = 0
        for ch in key:
            total += ord(ch)
        primed = total * 17
        index = primed % self.size
        return index

    def __getitem__(self, key):
        """
        Retrieves the value associated with a key.

        Args:
            key (str): The key to search for.

        Returns:
            value: The value associated with the key.

        Raises:
            KeyError: If the key does not exist in the hashtable.
        """
        value = self.values[self.hash(key)]
        if value is BLANK:
            raise KeyError(key)
        return value

    def __len__(self):
        """
        Returns the number of key-value pairs in the hashtable.

        Returns:
            int: The number of key-value pairs.
        """
        return len(self.values)

    def set(self, key, value):
        """
        Adds a new key-value pair to the hashtable.

        Args:
            key (str): The key of the pair.
            value: The value to be associated with the key.
        """
        index = self.hash(key)
        self.pairs[index] = (key, value)

    def get(self, key):
        """
        Retrieves the value associated with a key.

        Args:
            key (str): The key to search for.

        Returns:
            value: The value associated with the key, or None if the key does not exist.
        """
        index = self.hash(key)
        pair = self.pairs[index]
        if pair[0] == key:
            return pair[1]
        else:
            return None

    def __repr__(self):
        """
        Returns a string representation of the hashtable.

        Returns:
            str: A string representation of the hashtable.
        """
        string = ''
        for item in self:
            string += str(item)

        return string

    def list(self):
        """
        Returns a list of all the key-value pairs in the hashtable.

        Returns:
            list: A list of key-value pairs.
        """
        list = []
        for item in self._buckets:
            if item:
                list.append(item[:])

        return list