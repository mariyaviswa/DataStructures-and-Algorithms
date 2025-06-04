import time
"""
Time Complexity - O(n^2)
space complexity - O(1) 
"""
nums = list(map(int, input().rstrip().split()))
start = time.perf_counter()
for i in range(0, len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] > nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
end = time.perf_counter()
print(nums)
print("Total Time Taken :", (end-start)*(10**3))
