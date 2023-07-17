from insertion import insertion_sort

def test_reverse_sorted():
  input = [20, 18, 12, 8, 5, -2]
  sorted = insertion_sort(input)
  assert sorted == [-2, 5, 8, 12, 18, 20]

def test_few_uniques():
  input = [5, 12, 7, 5, 5, 7]
  sorted = insertion_sort(input)
  assert sorted == [5, 5, 5, 7, 7, 12]

def test_nearly_sorted():
  input = [2, 3, 5, 7, 13, 11]
  sorted = insertion_sort(input)
  assert sorted == [2, 3, 5, 7, 11, 13]
