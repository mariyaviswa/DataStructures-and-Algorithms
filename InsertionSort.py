"""
Insertion Sort
--------------

Time Complexity - O(n^2)
Space Complexity - O(1)

Here in Insertion sort we don't use swap method , we shifting all elements
"""


def sort(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1

        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]  # shifting elements
            j -= 1
        nums[j + 1] = key  # update the curr element


nums = list(map(int, input().rstrip().split()))
sort(nums)
print(nums)
