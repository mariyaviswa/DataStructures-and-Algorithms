from typing import List

"""
Merge Sort
----------
Working based on Divide and conquer
                 -------------------
Time complexity - O(n log(n))
Space complexity - O(n)

"""


def merge(arr: List[int], L: int, MID: int, R: int) -> None:
    left = arr[L: MID + 1]
    right = arr[MID + 1: R + 1]
    i, l, r = L, 0, 0

    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            arr[i] = left[l]
            l += 1
        else:
            arr[i] = right[r]
            r += 1
        i += 1
    while l < len(left):
        arr[i] = left[l]
        l, i = l + 1, i + 1
    while r < len(right):
        arr[i] = right[r]
        r, i = r + 1, i + 1


def mergeSort(arr: list[int], l: int, r: int) -> None:
    if l == r:
        return
    mid = (l + r) // 2
    mergeSort(arr, l, mid)
    mergeSort(arr, mid + 1, r)
    merge(arr, l, mid, r)


def sortArray(arr: list[int]) -> None:
    mergeSort(arr, 0, len(arr) - 1)


nums: list[int] = list(map(int, input().rstrip().split()))
sortArray(nums)  # Call the sortArray
print("Sorted array is: ", nums)