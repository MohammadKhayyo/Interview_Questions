import re


# 6. Searching Algorithms:
# • Implement the linear search algorithm.
# Searching an element in a list/array in python
# can be simply done using \'in\' operator
def Linear_Search_in_list_or_array(arr, x):
    if x in arr:
        return arr.index(x)
    return -1


# If you want to implement Linear Search in python
def search_1(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1


# This is similar to the above one, with the only difference
# being that it is using the recursive approach instead of iterative.
def recursive_Linear_Search(arr, curr_index, key):
    if curr_index == -1:
        return -1
    if arr[curr_index] == key:
        return curr_index
    return recursive_Linear_Search(arr, curr_index - 1, key)


def Linear_Search_Using_re_method(arr, x):
    arr_str = ','.join(str(i) for i in arr)

    # Use regular expression to search for the element in the string
    match = re.search(r'\b{}\b'.format(x), arr_str)

    # Output
    if match:
        # Calculate the index by counting the number of commas before the match
        result = arr_str[:match.start()].count(',')
        print(f"Element {x} is present at index {result}")
    else:
        print(f"Element {x} is not present in the array")


# • Implement the binary search algorithm.
# Python 3 program for recursive binary search.
# Returns index of x in arr if present, else -1
def recursive_binary_search(arr, low, high, x):
    # Check base case
    if high >= low:

        mid = (high + low) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return recursive_binary_search(arr, low, mid - 1, x)

        # Else the element can only be present in right subarray
        else:
            return recursive_binary_search(arr, mid + 1, high, x)

    else:
        # Element is not present in the array
        return -1


# Iterative Binary Search Function
# It returns index of x in given array arr if present, else returns -1
def Iterative_binary_search(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:

        mid = (high + low) // 2

        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1

        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1

        # means x is present at mid
        else:
            return mid

    # If we reach here, then the element was not present
    return -1


if __name__ == '__main__':
    # 6. Searching Algorithms:
    # • Implement the linear search algorithm.
    _arr = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]
    _x = 110
    print(Linear_Search_in_list_or_array(arr=_arr, x=_x))  # Element x is present at index 6
    _x = 175
    print(Linear_Search_in_list_or_array(arr=_arr, x=_x))  # Element x is not present in arr[].
    _x = 110
    print(recursive_Linear_Search(arr=_arr, curr_index=len(_arr) - 1, key=_x))  # Element x is present at index 6
    _x = 175
    Linear_Search_Using_re_method(arr=_arr, x=_x)  # Element x is not present in arr[].
    _x = 110
    Linear_Search_Using_re_method(arr=_arr, x=_x)  # Element x is present at index 6

    # • Implement the binary search algorithm.
    _arr = [2, 3, 4, 10, 40]
    _x = 10
    # Function call
    _result = recursive_binary_search(_arr, 0, len(_arr) - 1, _x)
    if _result != -1:
        print("Element is present at index", str(_result))
    else:
        print("Element is not present in array")
    # Function call
    result = Iterative_binary_search(_arr, _x)
    if result != -1:
        print("Element is present at index", str(result))
    else:
        print("Element is not present in array")
