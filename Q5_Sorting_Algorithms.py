# 5. Sorting Algorithms:
# • Implement the bubble sort algorithm.
def bubbleSort(arr):
    n = len(arr)
    # optimize code, so if the array is already sorted, it doesn't need
    # to go through the entire process
    swapped = False
    # Traverse through all array elements
    for i in range(n - 1):
        # range(n) also work but outer loop will repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        if not swapped:
            # if we haven't needed to make a single swap, we can just exit the main loop.
            return


def print_array(arr):
    for i in range(len(arr)):
        print("%d" % arr[i], end=" ")
    print()


# • Implement the merge sort algorithm.
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # create temp arrays
    L = [0] * n1
    R = [0] * n2

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    # Merge the temp arrays back into arr[l..r]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = l  # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


# l is for left index and r is right index of the
# sub-array of arr to be sorted


def mergeSort(arr, l, r):
    if l < r:
        # Same as (l+r)//2, but avoids overflow for large l and h
        m = l + (r - l) // 2

        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)


# • Implement the quicksort algorithm.
# Function to find the partition position
def partition(array, low, high):
    # choose the rightmost element as pivot
    pivot = array[high]
    # pointer for greater element
    i = low - 1
    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1
            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])
    # Swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    # Return the position from where partition is done
    return i + 1


# function to perform quicksort
def quickSort(array, low, high):
    if low < high:
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)
        # Recursive call on the left of pivot
        quickSort(array, low, pi - 1)
        # Recursive call on the right of pivot
        quickSort(array, pi + 1, high)


if __name__ == '__main__':
    # 5. Sorting Algorithms:
    # • Implement the bubble sort algorithm.
    _arr = [11, 64, 34, 25, 12, 22, 90]
    print("Unsorted Array before bubble Sort is:")
    print_array(_arr)
    bubbleSort(_arr)
    print('Sorted Array after bubble Sort is:')
    print_array(_arr)

    # • Implement the merge sort algorithm.
    _arr = [12, 11, 13, 5, 6, 7]
    n = len(_arr)
    print("Unsorted Array before merge sort is:")
    print_array(_arr)
    mergeSort(_arr, 0, n - 1)
    print('Sorted Array after merge sort is:')
    print_array(_arr)

    # • Implement the quicksort algorithm.
    _arr = [1, 7, 4, 1, 10, 9, -2]
    print("Unsorted Array before quick sort is:")
    print_array(_arr)
    size = len(_arr)
    quickSort(_arr, 0, size - 1)
    print('Sorted Array after quick sort is:')
    print(_arr)
