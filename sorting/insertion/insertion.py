def insert(sorted, value):
  i = 0
  while value > sorted[i]:
    i += 1
  while i < len(sorted):
    temp = sorted[i]
    sorted[i] = value
    value = temp
    i += 1
  sorted.append(value)

def insertion_sort(input):
  sorted = []
  sorted.append(input[0])
  for i in range(1, len(input)):
    insert(sorted, input[i])
  return sorted

if __name__ == "__main__":
  input = [8, 4, 23, 42, 16, 15]
  sorted = insertion_sort(input)
  print(sorted)
