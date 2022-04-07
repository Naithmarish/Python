input()
nums = [int(n) for n in input().split()]
minimum = nums[0]
maximum = nums[0]

for i in range(1, len(nums)):
    if nums[i] < minimum:
        minimum = nums[i]
    elif nums[i] > maximum:
        maximum = nums[i]
for i in range(1, len(nums)):
    if nums[i] == maximum:
        nums[i] = minimum
    elif nums[i] == minimum:
        nums[i] = maximum

print(*nums)