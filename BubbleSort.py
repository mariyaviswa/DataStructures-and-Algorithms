"""
Bubble Sort
-----------
Time Complexity - O(n^2)
Space Complexity  - O(1)

Basically it's checking and compare each element from start index 0 to last index
if meet the condition it will swap the elements
if n = 5 , arr = [5, 3, 8, 6, 7, 2]
    first iteration index 0 - len(nums)-1
    second iteration index 0 - len(nums)-2
    .
    .
    .
    last iteration index 0 - 1

"""


def sort(nums):
    for i in range(len(nums) - 1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]


nums = list(map(int, input().rstrip().split()))
sort(nums)
print(nums)
