def binary_search_string(names, target):
    names.sort()
    if len(names) == 0:
        return False

    middle = ((len(names)) - 1) // 2
    if names[middle] == target:
        return True

    if names[middle] > target:
        return binary_search_string(names[:middle], target)
    else:
        return binary_search_string(names[middle + 1:], target)


names = ["Viswa", "Ajay", "Rinoj", "Devadath", "Jerin", "Jeeva", "Harisan"]
print(binary_search_string(names, "Viswa"))  # True
print(binary_search_string(names, "Akash"))  # False
