"""• Analyze the time complexity of the sorting algorithms you implemented earlier."""
"""
1. Bubble Sort:
   - Bubble Sort is a simple comparison-based algorithm. In the worst case, it needs to go through the array `n-1` times (where `n` is the length of the array) and compare adjacent elements, swapping them if necessary.
   - The worst-case scenario occurs when the array is sorted in reverse order, leading to a time complexity of O(n²).
   - The best-case scenario is when the array is already sorted. The optimized code with the `swapped` flag allows the algorithm to detect this and stop early, resulting in a best-case time complexity of O(n).

2. Merge Sort:
   - Merge Sort is a divide-and-conquer algorithm. It divides the array into halves, recursively sorts each half, and then merges the sorted halves.
   - The division of the array into halves gives a time complexity of O(log n) for the recursive calls (since the array is halved in each call).
   - The merge operation for each level of recursion is O(n), as it needs to go through all the elements.
   - Therefore, the overall time complexity of Merge Sort is O(n log n), which applies to the worst case, average case, and best case.

3. QuickSort:
   - QuickSort is another divide-and-conquer algorithm. It selects a 'pivot' element and partitions the array into two halves, such that elements less than the pivot are on one side, and those greater are on the other. It then recursively sorts the two halves.
   - The average-case and best-case time complexity of QuickSort is O(n log n), similar to Merge Sort, due to the division of the array and the recursive sorting.
   - However, the worst-case time complexity is O(n²). This occurs when the pivot selection results in highly unbalanced partitions (for example, if the smallest or largest element is always chosen as the pivot).
   - The worst-case can be mitigated by using various strategies for choosing the pivot (like random selection or median-of-three), but the average-case time complexity remains O(n log n).

In summary:
- Bubble Sort has a time complexity of O(n²) in the worst case and O(n) in the best case.
- Merge Sort maintains a time complexity of O(n log n) in all cases.
- QuickSort generally performs at O(n log n) but can degrade to O(n²) in the worst case.
"""

######################################################################################################################

"""• Analyze the space complexity of the recursive programs you implemented earlier."""

"""
1. Space Complexity of the Factorial Function:
   - The `factorial` function uses recursion to calculate the factorial of a number `n`.
   - In each recursive call, the function decreases the value of `n` by 1 until it reaches the base case (`n == 1` or `n == 0`).
   - The maximum depth of the call stack, therefore, is `n`.
   - Thus, the space complexity of the factorial function is O(n), which represents the maximum number of function calls on the call stack at any point in time.

2. Space Complexity of the Permute Function:
   - The `permute` function uses recursion to generate all permutations of a given array `a`, between indices `l` (left) and `r` (right).
   - The function makes a recursive call for each element in the array, effectively reducing the problem size by 1 in each step (incrementing `l` by 1).
   - The maximum depth of recursion, and thus the height of the call stack, will be `r - l` at most, which represents the number of elements in the subarray being permuted.
   - Given the function's recursive nature, each recursive call consumes a certain amount of space on the stack. 
   - Therefore, the space complexity of the `permute` function is indeed O(r - l), which reflects the depth of the call stack based on the subarray size being permuted.

In summary:
- The factorial function has a space complexity of O(n), where `n` is the input number.
- The permute function has a space complexity of O(r - l), where `r` and `l` are the right and left indices of the subarray being permuted. This measure accounts for the depth of the recursion stack based on the size of the portion of the array being processed.
"""
