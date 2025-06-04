def recursive_binary_search(list, target):
    if len(list) == 0:  # if length of list of is zero then return false
        return False
    else:
        midpoint = (len(list)) // 2  # first state the midpoint

    if list[midpoint] == target:
        return True
    else:
        if list[midpoint] < target:
            '''
             if midpoint is less than target then sort the list from midpoint +1 to end of list index
            '''
            return recursive_binary_search(list[midpoint+1:], target)
        else:
            '''
            if midpoint is greater  than target then sort the list from [0] index  to midpoint of list index
            '''
            return recursive_binary_search(list[:midpoint], target)


def verify(index):
    print("Target found: ", index)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = recursive_binary_search(numbers, 12)
verify(result)

result = recursive_binary_search(numbers, 6)
verify(result)
