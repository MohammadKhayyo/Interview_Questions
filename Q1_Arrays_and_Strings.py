# 1. Arrays and Strings:
def reverse_string_in_place(s):
    """
    Returns the reversed version of the input string using slicing.
    """
    return s[::-1]


def find_max_min_optimal(arr):
    """
    Finds the maximum and minimum elements in an array using Python's built-in functions.
    """
    if not arr:
        return None, None
    return max(arr), min(arr)


def remove_duplicates_sorted_array_optimal(arr):
    """
    Removes duplicates from a sorted array efficiently.
    """
    # unique_elements = set(arr)
    # return list(unique_elements)
    return list(dict.fromkeys(arr))


if __name__ == "__main__":
    # 1. Arrays and Strings:
    # • Write a program to reverse a string in place.
    example_string = "Hello, world!"
    reversed_string = reverse_string_in_place(example_string)
    print(reversed_string)
    # • Write a program to find the maximum and minimum elements in an array.
    example_array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    max_elem_optimal, min_elem_optimal = find_max_min_optimal(example_array)
    print(f"max: {max_elem_optimal}, min: {min_elem_optimal}")
    # • Write a program to remove duplicates from a sorted array.
    sorted_array = [1, 1, 2, 2, 3, 4, 4, 5, 5, 5, 6]
    unique_array_optimal = remove_duplicates_sorted_array_optimal(sorted_array)
    print(unique_array_optimal)
