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

# @pytest.mark.skip("TODO")
def test_set_key_value():
    hashtable = Hashtable()
    hashtable.set("key", "value")
    assert hashtable.get("key") == "value"

# @pytest.mark.skip("TODO")
def test_retrieve_key_value():
    hashtable = Hashtable()
    hashtable.set("apple", "red")
    assert hashtable.get("apple") == "red"

# @pytest.mark.skip("TODO")
def test_key_not_exists():
    hashtable = Hashtable()
    assert hashtable.get("not_exists") == None

# @pytest.mark.skip("TODO")
def test_unique_keys():
    hashtable = Hashtable()
    hashtable.set("apple", "red")
    hashtable.set("banana", "yellow")
    hashtable.set("grape", "purple")
    unique_keys = [pair[0] for pair in hashtable.list() if pair[0] is not None]
    assert sorted(unique_keys) == ["apple", "banana", "grape"]

# @pytest.mark.skip("TODO")
def test_collision_handling():
    hashtable = Hashtable(3)
    hashtable.set("abc", "first")
    hashtable.set("bac", "second")
    assert hashtable.get("abc") == "first"
    assert hashtable.get("bac") == "second"

# @pytest.mark.skip("TODO")
def test_retrieve_value_from_collision_bucket():
    hashtable = Hashtable(3)
    hashtable.set("abc", "first")
    hashtable.set("bac", "second")
    assert hashtable.get("abc") == "first"

# @pytest.mark.skip("TODO")
def test_hash_key_in_range():
    hashtable = Hashtable(500)
    assert 0 <= hashtable.hash("test_key") < 500