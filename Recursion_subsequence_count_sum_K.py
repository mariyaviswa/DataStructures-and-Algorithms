"""
Print the count of subsequences whose sum is equal to k
-------------------------------------------------------
"""


def backtrack(i, total):
    if i == n:
        if total == k:
            return 1
        return 0
    # pick
    total += nums[i]
    left = backtrack(i + 1, total)

    # not pick
    total -= nums[i]
    right = backtrack(i + 1, total)

    return left + right


nums = list(map(int, input().split()))
k = int(input())
n = len(nums)
res = backtrack(0, 0)
print("Total subsequences: ", res)