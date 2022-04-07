input()
nums = [int(n) for n in input().split()]

minimum = nums[0]
for i in range(1, len(nums)):
    if nums[i] < minimum:
        minimum = nums[i]
print(minimum)