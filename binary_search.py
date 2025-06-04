# Binary search only applicable for sorted list in ascending order
"""
Time Complexity  - O(logn)
Space Complexity - O(1)
"""
"""
"""


def binary_search(list, target):
    list.sort()
    first = 0  # set the first position 0
    last = len(list) - 1  # set the last position last number in index
    while first <= last:  # if list non-empty then execute the below code
        midpoint = (first + last) // 2  # define the midpoint
        print(midpoint)
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
            print("first term updated to", first)
        else:
            last = midpoint - 1
            print("last term updated to", last)
    return None


def verify(index):
    if index is None:
        print("Target is not found in list")
    else:
        print("Target was found at index:", index)


numbers = [1, 2, 3, 4, 5, 6, 7, 8]
result = binary_search(numbers, 8)
verify(result)
