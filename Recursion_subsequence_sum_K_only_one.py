"""
Print only one subsequence whose sum is equal to K
--------------------------------------------------
"""


def backtrack(i, arr, total):
    if i == n:
        if total == k:
            res.append(arr.copy())
            return True
        return False
    # pick
    arr.append(nums[i])
    total += nums[i]
    if backtrack(i + 1, arr, total):
        return True
    # not pick
    total -= nums[i]
    arr.pop()
    if backtrack(i + 1, arr, total):
        return True
    return False


nums = list(map(int, input().split()))
k = int(input())
n = len(nums)
res = []
backtrack(0, [], 0)
print("subsequence: ", res)