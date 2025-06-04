"""
Print all subsequences
----------------------

Using pick or not pick intuition
"""


def backtrack(i, arr):
    if i == n:
        res.append(arr.copy())
        return
    # pick
    arr.append(nums[i])
    backtrack(i + 1, arr)
    # not pick
    arr.pop()
    backtrack(i + 1, arr)


nums = list(map(int, input().split()))
n = len(nums)
res = []
backtrack(0, [])
print("All subsequences: ", res)