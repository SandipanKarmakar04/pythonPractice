# 20. Write a program to split a list into two halves: nums = [1, 2, 3, 4, 5, 6].

nums = [1, 2, 3, 4, 5, 6]

mid = len(nums) // 2

fh = nums[:mid]
print(fh)

lh = nums[mid:]
print(lh)