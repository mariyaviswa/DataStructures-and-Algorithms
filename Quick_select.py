"""
Quick Select
------------

1) What does quick select do?
-----------------------------
  * Find the kth smallest element in an unordered list
  * In O(n) time instead of O(n logn) with sorting and linear search

Partition: (working steps)
--------------------------

 * Take a random element, this will be the pivot (usually last element)
 * Re-arrange elements in the list until
   * All elements smaller than pivot is on the left of pivot
   * All elements larger than pivot is on the right of pivot

Quik-Select working principles:
---------------------------------
 * partition the list according to random pivot
     * If random pivot is in index k - 1 then we found the answer ( Here k is the kth smallest (k))
     * Else , we do quick select
       1) on left partition if index > k-1
       2) on right partition if index < k-1

Big O Notations:
----------------

 Time Complexity ( Average Case) - O(n) {because we keep halving the array until we found the answer}
                 ( Worst Case) - O(n^2) {Here we don't shrink the array,  we remove one element for every iteration}
                                         {It Happens when pivot is always smallest/largest, sub-problem would be n-1 instead n/2}
 Space Complexity - O(logn) or O(1) (Depend on problems)
"""


def partition(arr, l, r):
    pivot = arr[r]
    i = l
    for j in range(l, r):
        if arr[j] <= pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i


def quickSelect(arr, l, r, k):
    pivot = partition(arr, l, r)

    if pivot == k - 1:
        return arr[k - 1]
    elif pivot < k - 1:
        return quickSelect(arr, pivot + 1, r, k)
    else:
        return quickSelect(arr, l, pivot - 1, k)


nums = list(map(int, input().rstrip().split()))
k = int(input())
if k == 1:
    suffix = "st"
elif k == 2:
    suffix = "nd"
elif k == 3:
    suffix = "rd"
else:
    suffix = "th"

result = quickSelect(nums, 0, len(nums) - 1, k)
print(f"The {k}-{suffix} smallest element is: ", result)
