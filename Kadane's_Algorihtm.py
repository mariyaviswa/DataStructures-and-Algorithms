"""
Kadane's algorithm
------------------

nums = [1, 2, 3, -2, 5]
curr = 0
max_sum = arr[0]

iterate for loop 0 to len(nums)
                curr            curr(update)       max_sum
                (0,0) = 0       0 + 1 = 1          (1,1) = 1
                (0,1) = 1       1 + 2 = 3          (1,3) = 3
                (0,3) = 3       3 + 3 = 6          (3,6) = 6
                (0,6) = 6       6 - 2 = 4          (6,4) = 6
                (0,4) = 4       4 + 5 = 9          (6,9) = 9 <---- This is the answer

"""


def finder(nums):
    curr, max_sum = 0, nums[0]

    for i in range(0, len(nums)):
        curr = max(0, curr)
        curr += nums[i]
        max_sum = max(max_sum, curr)

    return max_sum


nums = list(map(int, input().rstrip().split()))
print(finder(nums))
