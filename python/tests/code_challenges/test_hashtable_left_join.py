import pytest
from code_challenges.hashtable_left_join import left_join


def test_exists():
    assert left_join


# @pytest.mark.skip("TODO")
def test_example():
    synonyms = {
        "diligent": "employed",
        "fond": "enamored",
        "guide": "usher",
        "outfit": "garb",
        "wrath": "anger",
    }
    antonyms = {
        "diligent": "idle",
        "fond": "averse",
        "guide": "follow",
        "flow": "jam",
        "wrath": "delight",
    }

    expected = [
        ["fond", "enamored", "averse"],
        ["wrath", "anger", "delight"],
        ["diligent", "employed", "idle"],
        ["outfit", "garb", "NONE"],
        ["guide", "usher", "follow"],
    ]

    actual = left_join(synonyms, antonyms)

    assert actual == expected

def test_left_join_with_integers():
  synonyms = {
    1: 2,
    3: 4,
    5: 6,
  }
  antonyms = {
    2: 1,
    4: 3,
  }

  expected = [
    [1, 2, 1],
    [3, 4, 3],
    [5, 6, "NONE"],
  ]

  actual = left_join(synonyms, antonyms)

  assert actual == expected


def test_left_join_not_empty():
  synonyms = {}
  antonyms = {}

  expected = []

  actual = left_join(synonyms, antonyms)

  assert actual == expected