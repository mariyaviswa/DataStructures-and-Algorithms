def linear_search(list, target):
    """
    Return the index value if target found, else return none
    """
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None


def verify(index):
    if index is None:
        print("Target is not found in list")
    else:
        print("Target was found at index:", index)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = linear_search(numbers, 12)
verify(result)

result = linear_search(numbers, 6)
verify(result)
