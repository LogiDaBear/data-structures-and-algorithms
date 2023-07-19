from merge_sort import mergeSort, printList

# Test 1: Reverse-sorted
arr1 = [42, 23, 16, 15, 8, 4]
print("Test 1 - Reverse-sorted:")
print("Given array is")
printList(arr1)
mergeSort(arr1)
print("Sorted array is")
printList(arr1)
print()

# Test 2: Few uniques
arr2 = [8, 23, 8, 4, 15, 4]
print("Test 2 - Few uniques:")
print("Given array is")
printList(arr2)
mergeSort(arr2)
print("Sorted array is")
printList(arr2)
print()

# Test 3: Nearly-sorted
arr3 = [4, 8, 15, 16, 23, 42]
print("Test 3 - Nearly-sorted:")
print("Given array is")
printList(arr3)
mergeSort(arr3)
print("Sorted array is")
printList(arr3)
print()