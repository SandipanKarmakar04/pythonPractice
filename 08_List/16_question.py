# Write a program to find the second largest number in the list nums = [10, 20, 15, 40, 25].

nums = [10, 20, 15, 40, 25]
p = max(nums)
print(p)
nums.remove(p)
s = max(nums)
print(s)