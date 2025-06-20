"""
Selection Sort
--------------

    *At each iteration
    *set the curr value as min value
    *then search in whole array if any value less than our fixed value
      then set it as min value and swap with the current element
"""


def sort(nums):
    n = len(nums)
    for i in range(n):
        idx = i  # set the min value index
        for j in range(i + 1, n):
            if nums[j] < nums[idx]:
                idx = j # update the min value index
        nums[i], nums[idx] = nums[idx], nums[i]  # swap here


nums = list(map(int, input().rstrip().split()))
sort(nums)
print(nums)
