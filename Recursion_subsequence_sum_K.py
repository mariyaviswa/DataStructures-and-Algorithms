"""
Print the all subsequences whose sum is equal to K
--------------------------------------------------
"""


def backtrack(i, arr, total):
    if i == n:
        if total == k:
            res.append(arr.copy())
        return
    # pick
    arr.append(nums[i])
    total += nums[i]
    backtrack(i + 1, arr, total)
    # not pick
    total -= nums[i]
    arr.pop()
    backtrack(i + 1, arr, total)


nums = list(map(int, input().split()))
k = int(input())
n = len(nums)
res = []
backtrack(0, [], 0)
print("All subsequences: ", res)