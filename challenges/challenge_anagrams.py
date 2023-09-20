def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)


def is_anagram(first_string, second_string):
    """Faça o código aqui."""
    if not first_string and not second_string:
        return first_string, second_string, False

    first_string_sorted = "".join(quicksort(first_string.lower()))
    second_string_sorted = "".join(quicksort(second_string.lower()))

    are_anagrams = first_string_sorted == second_string_sorted

    return first_string_sorted, second_string_sorted, are_anagrams
    raise NotImplementedError
