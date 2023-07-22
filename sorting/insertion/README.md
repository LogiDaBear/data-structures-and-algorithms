# Blog Notes: Insertion Sort

## Code Challenge 26
Review the pseudocode below, then trace the algorithm by stepping through the process with the provided sample array. Document your explanation by creating a blog article that shows the step-by-step output after each iteration through some sort of visual.
![pseudocode example](pseudoCC26.jpg)
Once you are done with your article, code a working, tested implementation of Insertion Sort based on the pseudocode provided.

## Whiteboard Process
blog article

## Blog

Step-by-Step Process of Insertion Sort

1. Starting arrays

- input array: [8, 4, 23, 42, 16, 15]
- sorted array: []

2. First Iteration (Insert 8)

- input array: [8, 4, 23, 42, 16, 15]
- sorted array: [8]
- The first element of the input array (8) is placed in the sorted array since it is the only element.

3. Second Iteration (Insert 4)

- input array: [8, 4, 23, 42, 16, 15]
- sorted array: [4, 8]
- The second element of the input array (4) is compared with the elements in the sorted array (8). As 4 is smaller than 8, it is inserted before 8, resulting in [4, 8].

4. Third Iteration (Insert 23)

- input array: [8, 4, 23, 42, 16, 15]
- sorted array: [4, 8, 23]
- The third element of the input array (23) is compared with the elements in the sorted array (4, 8). As 23 is greater than 8, it is inserted after 8, resulting in [4, 8, 23].

5. Fourth Iteration (Insert 42)

- input array: [8, 4, 23, 42, 16, 15]
- sorted array: [4, 8, 23, 42]
- The fourth element of the input array (42) is compared with the elements in the sorted array (4, 8, 23). As 42 is greater than 23, it is inserted after 23, resulting in [4, 8, 23, 42].

6. Fifth Iteration (Insert 16)

- input array: [8, 4, 23, 42, 16, 15]
- sorted array: [4, 8, 16, 23, 42]
- The fifth element of the input array (16) is compared with the elements in the sorted array (4, 8, 23, 42). As 16 is greater than 8 and less than 23, it is inserted between 8 and 23, resulting in [4, 8, 16, 23, 42].

7. Sixth Iteration (Insert 15)

- input array: [8, 4, 23, 42, 16, 15]
- sorted array: [4, 8, 15, 16, 23, 42]
- The sixth element of the input array (15) is compared with the elements in the sorted array (4, 8, 16, 23, 42). As 15 is greater than 8 and less than 16, it is inserted between 8 and 16, resulting in [4, 8, 15, 16, 23, 42].


## Approach & Efficiency
Big0-Space:O(n)
Time:O(1)

## Attributions & References
Class 401d22, [geeksforgeeks](https://www.geeksforgeeks.org/insertion-sort/)

## Solution
[sorting/insertion/insertion.py](sorting/insertion/insertion.py)