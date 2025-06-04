"""
ORDERED DICTIONARY
------------------

It is mainly used in LRU cache - (Least Recently Used)
and ordered dict implemented using doubly linked list
`OrderedDict` maintains the sequence in which keys are added, ensuring that the order is preserved during iteration.
                                                             -------------------------------------------------------
In contrast, a standard dictionary does not guarantee any specific order when iterated,
providing values in an arbitrary sequence.
`OrderedDict` distinguishes itself by retaining the original insertion order of items.

Time Complexity:
----------------
    Operation                  Time
    ----------                ------

    Get item(Key):             O(1)
    Set item(key, value):      O(1)
    Delete item(key):          O(n)
    Iteration:                 O(n)


Operation	                                                Function	                                Time Complexity
----------                                                ----------------                            --------------------

Insertion	                                             od[key] = value	                                 O(1)
Lookup (Get Value)	                                     od[key]	                                         O(1)
Update Value                                          	 od[key] = new_value	                             O(1)
Deletion	                                             del od[key]	                                     O(1)
Check Key Presence	                                     key in od	                                         O(1)
Iteration (Forward)	                                     for key in od:	                                     O(N)
Iteration (Reverse)                     	             reversed(od)	                                     O(N)
Move Key to End	                                         od.move_to_end(key)	                             O(1)
Move Key to Start	                                     od.move_to_end(key, last=False)	                 O(1)
Pop Last Item	                                         od.popitem()	                                     O(1)
Pop First Item	                                         od.popitem(last=False)                              O(1)
"""


from collections import OrderedDict

nums = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(nums)
print("------------------------------")
# update the ordered dictionary
nums.update([('d', 4), ('e', 5), ('f', 6)])
print("AfterUpdating: ", nums)

# pop the last item
last = nums.popitem(last=True)
print("Last item: ", last)

# pop the first item
first = nums.popitem(last=False)
print("First Item: ", first)


# Update the dict
nums.update([('a', 1)])

# print the dict
print(nums)

# Move the item to first or beginning
nums.move_to_end('a', last=False)
print("After Moving to first: ", nums)

# Moving the item to last or end
nums.move_to_end('a', last=True)
print("After Moving to last: ", nums)

# pop the key
nums.pop('c')
print("After removing key: 'c' : ", nums)