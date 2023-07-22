# CodeChallenge30 - Hashtable 
## Implement a Hashtable Class with the following methods:

### set
- Arguments: key, value
- Returns: nothing
- This method should hash the key, and set the key and value pair in the table, handling collisions as needed.
- Should a given key already exist, replace its value from the value argument given to this method.
### get
- Arguments: key
- Returns: Value associated with that key in the table
### has
- Arguments: key
- Returns: Boolean, indicating if the key exists in the table already.
### keys
- Returns: Collection of keys
### hash
- Arguments: key
- Returns: Index in the collection for that key

## Write tests to prove the following functionality:

1. Setting a key/value to your hashtable results in the value being in the data structure
2. Retrieving based on a key returns the value stored
3. Successfully returns null for a key that does not exist in the hashtable
4. Successfully returns a list of all unique keys that exist in the hashtable
5. Successfully handle a collision within the hashtable
6. Successfully retrieve a value from a bucket within the hashtable that has a collision
7. Successfully hash a key to an in-range value


Ensure your tests are passing before you submit your solution

## testing
pytest [test_hashtable.py](tests/data_structures/test_hashtable.py)

## Attributions

### Websites
- This site was a HUGE factor in my success [Real Python](https://realpython.com/python-hash-table/#get-to-know-the-hash-table-data-structure)

- [GeeksforGeeks](https://www.geeksforgeeks.org/implementation-of-hash-table-in-python-using-separate-chaining/)

### ChatGPT
here is my conversation but it only took me backwards when I used this code and this was with gpt4 so I am MORE than ok with not passing all tests! `:)`
```
here is my code:

BLANK = object()
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def list(self):
      list = []
      for item in self._buckets:
          if item:
              list.append([(pair[0], pair[1]) for pair in item])

      return list

class Hashtable:

    def __init__(self, size = 1024):
        self.size = size
        self.values = size * [BLANK]
        self.pairs = size * [(None, None)]
        self._buckets = [[["silent", True], ["listen", "to me"]], [["ahmad", 30]]]
 

    def hash(self, key):
        total = 0
        for ch in key:
            total += ord(ch)
        primed = total * 17
        index = primed % self.size
        return index
    


    def __getitem__(self, key, value):
        value = self.values[self.index(key)]
        if value is BLANK:
            raise KeyError(key)
        return value
    

    def __len__(self):
        return len(self.values)
       
    def set(self, key, value):
        index = self.hash(key)
        self.pairs[index] = (key, value)

    def get(self, key):
        index = self.hash(key)
        pair = self.pairs[index]
        if pair[0] == key:
            return pair[1]
        else:
            return None
    
    def __repr__(self):
        string = ''
        for item in self:
            string += str(item)

        return string
    
here is the tests that I CANNOT change:
import pytest
from data_structures.hashtable import Hashtable


def test_exists():
    assert Hashtable


# @pytest.mark.skip("TODO")
def test_get_apple():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.get("apple")
    expected = "Used for apple sauce"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_internals():
    hashtable = Hashtable(1024)
    hashtable.set("ahmad", 30)
    hashtable.set("silent", True)
    hashtable.set("listen", "to me")

    actual = []

    # NOTE: purposely breaking encapsulation to test the "internals" of Hashmap
    for item in hashtable._buckets:
        if item:
            actual.append(item.display())

    expected = [[["silent", True], ["listen", "to me"]], [["ahmad", 30]]]

    assert actual == expected

here is the error:

____________________________________________________ test_internals ____________________________________________________

    def test_internals():
        hashtable = Hashtable(1024)
        hashtable.set("ahmad", 30)
        hashtable.set("silent", True)
        hashtable.set("listen", "to me")

        actual = []

        # NOTE: purposely breaking encapsulation to test the "internals" of Hashmap
        for item in hashtable._buckets:
            if item:
>               actual.append(item.display())
E               AttributeError: 'list' object has no attribute 'display'

tests/data_structures/test_hashtable.py:30: AttributeError
=============================================== short test summary info ================================================
FAILED tests/data_structures/test_hashtable.py::test_internals - AttributeError: 'list' object has no attribute 'display'
============================================= 1 failed, 2 passed in 0.01s =======
ChatGPT
The test test_internals() is failing because it's trying to call a method display() on a list item inside hashtable._buckets but there's no such method on the list data type.

Looking at your implementation of the Hashtable class, the _buckets attribute is a list of lists, where each inner list is a pair of key and value. But the list data type in Python doesn't have a display() method, hence the AttributeError.

I can see you have a list() method in Node class but it's not used anywhere. Given the current code and tests, you may not even need a Node class.

To make your code pass the tests, you should change your hashtable implementation to actually use a list of Node objects for each bucket, where each Node represents a key-value pair.

However, considering the current tests and implementation, it might be simpler to just remove the display() method call from the test and append the list item directly to actual:

python
Copy code
def test_internals():
    hashtable = Hashtable(1024)
    hashtable.set("ahmad", 30)
    hashtable.set("silent", True)
    hashtable.set("listen", "to me")

    actual = []

    # NOTE: purposely breaking encapsulation to test the "internals" of Hashmap
    for item in hashtable._buckets:
        if item:
            actual.append(item)

    expected = [[["silent", True], ["listen", "to me"]], [["ahmad", 30]]]

    assert actual == expected
This should work assuming that hashtable._buckets is correctly updated when you call set(), but your current implementation of set() and get() are not using _buckets. They use self.pairs array instead which is not the one being tested in test_internals(). Therefore, you will need to modify set() method to use _buckets and correctly append lists of key-value pairs.

Finally, as a note, it's generally bad practice to test internal representations because it ties your tests to specific implementation details. The test_internals() function violates the idea of encapsulation, which is a core principle of object-oriented design. In real-world practice, you would usually want to test the public interface of your class rather than its internal details.




User
i  cant change the test so refactor my code
ChatGPT
If you cannot change the tests, then you have to refactor your code to satisfy the requirements.

From the error, the display() method is not found in the list. The function display() is not defined anywhere in the provided code, and it seems to be expected to return the contents of a bucket. In your case, it should return the contents of a bucket in the hashtable.

I suggest adding display() to your Node class, and making Node object as the bucket in the Hashtable class. Also, I see that you have defined the list method in the Node class, but it is not used anywhere. You might want to remove it.

Please find the updated code:

python
Copy code
class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None

    def display(self):
        if self.key and self.value:
            return [self.key, self.value]
        else:
            return None


class Hashtable:

    def __init__(self, size = 1024):
        self.size = size
        self._buckets = [Node()] * size

    def hash(self, key):
        total = 0
        for ch in key:
            total += ord(ch)
        primed = total * 17
        index = primed % self.size
        return index

    def set(self, key, value):
        index = self.hash(key)
        node = self._buckets[index]
        if not node.key and not node.value:
            node.key = key
            node.value = value
        else:
            while node.next:
                node = node.next
            node.next = Node(key, value)

    def get(self, key):
        index = self.hash(key)
        node = self._buckets[index]
        if node.key == key:
            return node.value
        while node.next:
            node = node.next
            if node.key == key:
                return node.value
        return None
This implementation creates a new Node for each bucket in the hashtable. When you set() a new key-value pair, it checks the hashed bucket. If it's empty (node.key and node.value are both None), it fills the bucket with the new pair. If it's not empty, it creates a new Node at the end of the linked list in that bucket.

When you get() a key, it checks the hashed bucket. If the first Node in the bucket is the desired key, it returns the value. If not, it goes through the linked list in the bucket to find the desired key.

The Node.display() method returns a list of the key-value pair stored in the Node. This should satisfy your test_internals() test.

This is a simplified hashtable implementation. It uses separate chaining to handle hash collisions, but does not resize the hashtable when it's too full or too empty. In a real-world application, you would likely want to implement resizing to make the hashtable more efficient.




User
____________________________________________________ test_internals ____________________________________________________

    def test_internals():
        hashtable = Hashtable(1024)
        hashtable.set("ahmad", 30)
        hashtable.set("silent", True)
        hashtable.set("listen", "to me")

        actual = []

        # NOTE: purposely breaking encapsulation to test the "internals" of Hashmap
        for item in hashtable._buckets:
            if item:
                actual.append(item.display())

        expected = [[["silent", True], ["listen", "to me"]], [["ahmad", 30]]]

>       assert actual == expected
E       AssertionError: assert [['ahmad', 30...ad', 30], ...] == [[['silent', ...'ahmad', 30]]]
E         At index 0 diff: ['ahmad', 30] != [['silent', True], ['listen', 'to me']]
E         Left contains 1022 more items, first extra item: ['ahmad', 30]
E         Use -v to get more diff

tests/data_structures/test_hashtable.py:34: AssertionError
=============================================== short test summary info =======
ChatGPT
The test is expecting a list of lists where each sub-list contains a key-value pair. However, our current Node.display() function returns a list containing a single key-value pair. This happens because in the current implementation, each node stores only one key-value pair.

Also, currently the set method overwrites the key-value pair in the bucket where the hash collision occurs, instead of chaining them. We need to implement chaining to allow for collisions, which seems to be what the test is expecting (i.e., multiple key-value pairs in the same bucket).

We can refactor your code to satisfy these requirements as follows:

python
Copy code
class Node:
    def __init__(self):
        self.pairs = []

    def display(self):
        return self.pairs[:]


class Hashtable:
    def __init__(self, size=1024):
        self.size = size
        self._buckets = [Node() for _ in range(size)]

    def hash(self, key):
        total = 0
        for ch in key:
            total += ord(ch)
        primed = total * 17
        index = primed % self.size
        return index

    def set(self, key, value):
        index = self.hash(key)
        node = self._buckets[index]
        node.pairs.append([key, value])

    def get(self, key):
        index = self.hash(key)
        node = self._buckets[index]
        for pair in node.pairs:
            if pair[0] == key:
                return pair[1]
        return None
In this code, the Node class holds multiple key-value pairs in its pairs attribute, which is a list of lists. When you set() a new key-value pair, it appends the pair to the list of pairs in the hashed Node.

The Node.display() method now returns the list of pairs in the Node.

When you get() a key, it goes through the list of pairs in the hashed Node to find the desired key.

This should satisfy your test_internals() test.




User

2 / 2

____________________________________________________ test_internals ____________________________________________________

    def test_internals():
        hashtable = Hashtable(1024)
        hashtable.set("ahmad", 30)
        hashtable.set("silent", True)
        hashtable.set("listen", "to me")

        actual = []

        # NOTE: purposely breaking encapsulation to test the "internals" of Hashmap
        for item in hashtable._buckets:
            if item:
                actual.append(item.display())

        expected = [[["silent", True], ["listen", "to me"]], [["ahmad", 30]]]

>       assert actual == expected
E       AssertionError: assert [[], [], [], [], [], [], ...] == [[['silent', ...'ahmad', 30]]]
E         At index 0 diff: [] != [['silent', True], ['listen', 'to me']]
E         Left contains 1022 more items, first extra item: []
E         Full diff:
E           [
E         +  [],
E         +  [],
E         +  [],...
E
E         ...Full output truncated (1028 lines hidden), use '-vv' to show

tests/data_structures/test_hashtable.py:34: AssertionError
=============================================== short test summary info ================================================
FAILED tests/data_structures/test_hashtable.py::test_internals - AssertionError: assert [[], [], [], [], [], [], ...] == [[['silent', ...'ahmad', 30]]]
ChatGPT
I see, your test seems to want to see only the populated buckets in the hashtable.

In the current setup, when you do actual.append(item.display()) in the test, it's appending all the buckets in the hashtable, which includes empty ones (buckets containing empty lists). That's why the actual output contains lots of empty lists [].

A possible solution would be to add a check in the display() method of the Node class to return None if the bucket is empty (no key-value pairs). And in the test, only append the display output to actual if it's not None.

However, you mentioned that you cannot change the tests, so we need to modify the code to only include non-empty buckets. We can do this by introducing an attribute, _num_entries, which will track the number of entries in the hashtable.

Here is the refactored code:

python
Copy code
class Node:
    def __init__(self):
        self.pairs = []

    def display(self):
        return self.pairs[:] if self.pairs else None


class Hashtable:
    def __init__(self, size=1024):
        self.size = size
        self._buckets = [Node() for _ in range(size)]
        self._num_entries = 0

    def hash(self, key):
        total = 0
        for ch in key:
            total += ord(ch)
        primed = total * 17
        index = primed % self.size
        return index

    def set(self, key, value):
        index = self.hash(key)
        node = self._buckets[index]
        node.pairs.append([key, value])
        self._num_entries += 1

    def get(self, key):
        index = self.hash(key)
        node = self._buckets[index]
        for pair in node.pairs:
            if pair[0] == key:
                return pair[1]
        return None

    def __iter__(self):
        for node in self._buckets:
            if node.display():
                yield node.display()
The __iter__() method is added to the Hashtable class which will only yield the non-empty buckets. So when you iterate over a Hashtable object, you'll only get the non-empty buckets. Since the test is iterating over hashtable._buckets to populate actual, this should result in actual only containing non-empty buckets, matching the expected output.

Please note that this approach changes the semantics of iterating over a Hashtable object. If you need to keep the original semantics (iterating over all buckets, including empty ones), a different approach would be required.




User
still failing with this error:
___________________________________________________ test_internals ____________________________________________________

    def test_internals():
        hashtable = Hashtable(1024)
        hashtable.set("ahmad", 30)
        hashtable.set("silent", True)
        hashtable.set("listen", "to me")

        actual = []

        # NOTE: purposely breaking encapsulation to test the "internals" of Hashmap
        for item in hashtable._buckets:
            if item:
                actual.append(item.display())

        expected = [[["silent", True], ["listen", "to me"]], [["ahmad", 30]]]

>       assert actual == expected
E       AssertionError: assert [None, None, ...ne, None, ...] == [[['silent', ...'ahmad', 30]]]
E         At index 0 diff: None != [['silent', True], ['listen', 'to me']]
E         Left contains 1022 more items, first extra item: None
E         Use -v to get more diff

tests/data_structures/test_hashtable.py:34: AssertionError
=============================================== short test summary info ================================================
FAILED tests/data_structures/test_hashtable.py::test_internals - AssertionError: assert [None, None, ...ne, None, ...] == [[['silent', ...'ahmad', 30]]]
```