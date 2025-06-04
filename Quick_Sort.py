"""
Quick Sort
----------

1) What does quick sort do?
-----------------------------
  * It will sort the array in O(n logn) time using partition
  * Using recursion method it will work

Partition: (working steps)
--------------------------

 * Take a random element, this will be the pivot (usually last element)
 * Re-arrange elements in the list until
   * All elements smaller than pivot is on the left of pivot
   * All elements larger than pivot is on the right of pivot

Sample:
-------

[4,3,2,1,5,6,7,9]
step 1 --> choose an element. It may be the (Example, choose 4, index 0)
          1) first element
          2) last element ( most of the time)
          3) mid-element
          4) or randomly choose
step 2 --> pick up a pivot and place the pivot in that correct place [3,2,1,4,5,6,7,9]
step 3 --> change the array
            pivot = 4
            1) the left side of pivot smaller than pivot's value --> [3,2,1,4,5,6,7,9]
                                                                     ------
            2) the right side of pivot greater than pivot's value --> [3,2,1,4,5,6,7,9]
                                                                              ---------
step 4 --> do this in recursion until sorted

Quik-Sort working principles:
---------------------------------
     * partition the list first
     * Then partition the left portion and right portion
     * Until the right pointer less than or equal to left pointer, if not, return

Big O Notations:
----------------

Time Complexity ( Average Case) - O(n logn) {because we keep halving the array until we found the answer i.e, n/2}
                 ( Worst Case) - O(n^2) {Here we don't shrink the array,  we remove one element for every iteration}
                                         {It Happens when pivot is always smallest/largest, sub-problem would be n-1 instead n/2}

Space Complexity - O(1) , because we don't need to use extra space instead we replace value in-place
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


def quickSort(arr, l, r):
    if r <= l:
        return

    pivot = partition(arr, l, r)

    quickSort(arr, l, pivot - 1)  # left portion
    quickSort(arr, pivot + 1, r)  # right portion


nums = list(map(int, input().rstrip().split()))  # list of input array
quickSort(nums, 0, len(nums) - 1)  # call the function to sort the array
print("The sorted array: ", nums)
