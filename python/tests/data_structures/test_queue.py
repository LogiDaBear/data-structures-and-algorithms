import pytest
from data_structures.queue import Queue
from data_structures.invalid_operation_error import InvalidOperationError


def test_exists():
    assert Queue


# @pytest.mark.skip("TODO")
def test_enqueue():
    q = Queue()
    q.enqueue("apple")
    actual = q.front.value
    expected = "apple"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_dequeue():
    q = Queue()
    q.enqueue("apple")
    q.enqueue("banana")
    actual = q.dequeue()
    expected = "apple"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_peek():
    q = Queue()
    q.enqueue("apple")
    q.enqueue("banana")
    q.enqueue("cucumber")
    actual = q.peek()
    expected = "apple"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_peek_when_empty():
    q = Queue()
    with pytest.raises(InvalidOperationError):
        q.peek()


# @pytest.mark.skip("TODO")
def test_enqueue_one():
    q = Queue()
    q.enqueue("apples")
    actual = q.peek()
    expected = "apples"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_enqueue_two():
    q = Queue()
    q.enqueue("apples")
    q.enqueue("bananas")
    actual = q.peek()
    expected = "apples"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_dequeue_when_empty():
    q = Queue()
    with pytest.raises(InvalidOperationError):
        q.dequeue()


# @pytest.mark.skip("TODO")
def test_dequeue_when_full():
    q = Queue()
    q.enqueue("apples")
    q.enqueue("bananas")
    actual = q.dequeue()
    expected = "apples"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_peek_post_dequeue():
    q = Queue()
    q.enqueue("apples")
    q.enqueue("bananas")
    q.dequeue()
    actual = q.peek()
    expected = "bananas"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_is_empty():
    q = Queue()
    actual = q.is_empty()
    expected = True
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_exhausted():
    q = Queue()
    q.enqueue("apple")
    q.enqueue("banana")
    q.enqueue("cucumber")
    q.dequeue()
    q.dequeue()
    q.dequeue()
    actual = q.is_empty()
    expected = True
    assert actual == expected

def test_can_enqueue_into_queue():
    queue = Queue()
    queue.enqueue(1)
    assert queue.front.value == 1

def test_can_enqueue_multiple_values_into_queue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.front.value == 1
    assert queue.rear.value == 2

def test_can_dequeue_out_of_a_queue_the_expected_value():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    value = queue.dequeue()
    assert value == 1
    assert queue.front.value == 2

def test_can_peek_into_a_queue_seeing_the_expected_value():
    queue = Queue()
    queue.enqueue(1)
    value = queue.peek()
    assert value == 1

def test_can_successfully_empty_a_queue_after_multiple_dequeues():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.dequeue()
    queue.dequeue()
    assert queue.is_empty()

def test_can_successfully_instantiate_an_empty_queue():
    queue = Queue()
    assert queue.is_empty()

def test_calling_dequeue_or_peek_on_empty_queue_raises_exception():
    queue = Queue()
    with pytest.raises(InvalidOperationError):
        queue.dequeue()

    with pytest.raises(InvalidOperationError):
        queue.peek()