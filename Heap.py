"""
HEAP
----
A heap queue or priority queue is a data structure that allows us to quickly access the smallest (min-heap)
or largest (max-heap) element. A heap is typically implemented as a binary tree, where each parent node’s value is smaller
 (for a min-heap) or larger (for a max-heap) than its children. However, in Python,
heaps are usually implemented as min-heaps which means the smallest element is always at the root of the tree,
 making it easy to access.

Summary of Time Complexities
----------------------------
    Operation	                                         Function                                 	Time Complexity
    ---------                                           -----------                                ------------------
    Heapify	                                           heapq.heapify(list)                           	O(N)
    Insertion	                                       heapq.heappush(heap, item)                      	O(log N)
    Get Minimum	                                       heap[0]	                                        O(1)
    Delete Minimum	                                   heapq.heappop(heap)	                            O(log N)
    Push & Pop Together	                               heapq.heappushpop(heap, item)	                O(log N)
    Replace Root	                                   heapq.heapreplace(heap, item)	                O(log N)
    Find k Smallest Elements                           heapq.nsmallest(k, iterable)                 	O(N log k)
    Find k Largest Elements	                           heapq.nlargest(k, iterable)	                    O(N log k)

"""


import heapq

minHeap = [4, 5, 3, 2, 7, 6, 10, 9, 1, 8]

# heapify the list - O(n)
heapq.heapify(minHeap)
print("Min Heap: ",  minHeap)

# peek element without removing - O(1)
print("Peek: ", minHeap[0])

# peek with removing - O(logn)
print("PEEK: ", heapq.heappop(minHeap))
print("Min Heap: ", minHeap)

# push in Heap - O(logn)
heapq.heappush(minHeap, 1)
print("After Pushing: ", minHeap)

# it will replace the value we have given, with the peek in heap - O(logn)
heapq.heapreplace(minHeap, 0)
print("After replacing: ", minHeap)

# push and pop at a time
heapq.heappushpop(minHeap, 1)
print("After pushing and popping at a time: ", minHeap)

# Find nsmallest in heap
largest = heapq.nlargest(3, minHeap)
print("Top 3 largest elements: ", largest)

smallest = heapq.nsmallest(3, minHeap)
print("Top 3 smallest elements: ", smallest)

minHeap1 = [12, 11, 13, 15, 14, 15]
mergedHeap = list(heapq.merge(minHeap, minHeap1))
print("After merging: ", mergedHeap)