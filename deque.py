from collections import deque

"""
Deque  (List- like container with fast append and pops on either end)
-----
    ** It is faster than list ** 
Deque support thread-safe. memory efficient appends and pops from either side of the deque with approximately the same 0(1) performance in
either direction.

A deque stands for Double-Ended Queue. It is a data structure that allows adding and removing elements from both ends efficiently. 
Unlike regular queues, which are typically operated on using FIFO (First In, First Out) principles, 
a deque supports both FIFO and LIFO (Last In, First Out) operations.

Deques are a generalization of stacks and queues (the name is pronounced “deck” and is short for “double-ended queue”). 
Deques support thread-safe, memory efficient appends and pops from either side of the deque with 
approximately the same O(1) performance in either direction.

Though list objects support similar operations, they are optimized for fast fixed-length operations and incur O(n) memory movement 
costs for pop(0) and insert(0, v) operations which change both the size and position of the underlying data representation.

If maxlen is not specified or is None, deques may grow to an arbitrary length. Otherwise, the deque is bounded to the specified maximum length. 
Once a bounded length deque is full, when new items are added, a corresponding number of items are discarded from the opposite end. 
Bounded length deques provide functionality similar to the tail filter in Unix. 
They are also useful for tracking transactions and other pools of data where only the most recent activity is of interest.

Example:
-------
            [1, 2,, 3, 4, 5]
             ^            ^
             |            |
             Rear         Front
             
You can add and remove both from rear and end of the deque.

Operation	          Description	                                                                             Time Complexity
---------             ------------                                                                               ----------------

append(x)	              Adds x to the right end of the deque.	                                                            O(1)
appendleft(x)	          Adds x to the left end of the deque.	                                                            O(1)
pop()	                  Removes and returns an element from the right end of the deque.	                                O(1)
popleft()	              Removes and returns an element from the left end of the deque.	                                O(1)
extend(iterable)	      Adds all elements from iterable to the right end of the deque.	                                O(k)
extendleft(iterable)	  Adds all elements from iterable to the left end of the deque (reversed order).	                O(k)
remove(value)	          Removes the first occurrence of value from the deque. Raises ValueError if not found.	            O(n)
rotate(n)	              Rotates the deque n steps to the right. If n is negative, rotates to the left.	                O(k)
clear()	                  Removes all elements from the deque.	                                                            O(n)
count(value)	          Counts the number of occurrences of value in the deque.	                                        O(n)
index(value)	          Returns the index of the first occurrence of value in the deque. Raises ValueError if not found.	O(n)
reverse()	              Reverses the elements of the deque in place.	O(n)


Appending and Deleting Dequeue Items
------------------------------------
append(x):                         Adds x to the right end of the deque.
appendleft(x):                     Adds x to the left end of the deque.
extend(iterable):                  Adds all elements from the iterable to the right end.
extendleft(iterable):              Adds all elements from the iterable to the left end (in reverse order).
remove(value):                     Removes the first occurrence of the specified value from the deque. If value is not found, 
                                   it raises a ValueError.
pop():                             Removes and returns an element from the right end.
popleft():                         Removes and returns an element from the left end.
clear():                           Removes all elements from the deque.


In addition to the above, deques support iteration, pickling, len(d), reversed(d), copy.copy(d), 
copy.deepcopy(d), membership testing with the in operator, and subscript references such as d[0] to access the first element. 
Indexed access is O(1) at both ends but slows to O(n) in the middle. For fast random access, use lists instead.

pickling
--------

In Python, pickling is the process of converting a Python object into a byte stream, 
which can then be stored in a file or transferred over a network. This process is also known as serialization. 
The reverse process, converting a byte stream back into a Python object, is called unpickling or deserialization.

"""
arr = deque()

print("arr Before: ", arr)
# append the element to the front or right
arr.append(2)
print("After append: ", arr)

# append the element to the rear or left
arr.appendleft(1)
print("After appendleft: ", arr)

print("arr After: ", arr)

print("----------------------------------------------")

# we can initialize the deque as default

nums = deque([1, 2, 3, 4, 5])

print("Nums Before: ", nums)

# extend the deque to the right (iterable)
nums.extend([6, 7, 8, 9, 10])
print("After Extend: ", nums)

# extend the deque to the left (iterable)
nums.extendleft([1, 2, 3, 4])
print("After extend-left: ", nums)

# pop from the front(right)
nums.pop()
print("After pop: ", nums)

# pop from rear(left)
nums.popleft()
print("After popleft: ", nums)

# remove the value
nums.remove(9)
print("After remove(9): ", nums)

# count the value
cnt = nums.count(1)
print("count(1): ", cnt)

# rotate the deque
nums.rotate(2)  # rotate the deque 2 steps to the right
print("After rotate(right): ", nums)

# rotate the deque
nums.rotate(-2)  # rotate the deque 2 steps to the left
print("After rotate(right): ", nums)

# reverse the deque using reverse() and reversed
nums.reverse()
print("After reverse: ", nums)

# reversed(nums) it will through the error
print("After reversing: ", deque(reversed(nums)))

# max-len of deque
length = nums.maxlen
print("Max length of nums: ", length)

# Find the index of the value
idx = nums.index(8)
print("The index of 8 is: ", idx)

# Insert the element or anything into the deque
nums.insert(0, 9)  # (index pos, val)
print("After Insertion: ", nums)

# clear the deque
nums.clear()
print("After clear: ", nums)

print("Nums After: ", nums)

nums1 = deque(maxlen=5)
print("Max-len: ", nums1.maxlen)

# Here I initialized the deque with the max-len
# If I try to do add more numbers with high of the max-len then it will remove the old one
for i in range(0, 10):
    nums1.append(i)
    # Here You can see after it reach the maximum length
    # then if any value comes in it will remove the old one (i.e, from the left most)
    print("The array nums1: ", nums1)