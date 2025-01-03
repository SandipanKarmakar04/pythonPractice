# Write a Python program to find the common elements between two tuples.

t1 = (2,4,6,7,8,9,2)
t2 = (2,4,6,5,9,8,1)

common = tuple(set(t1) & set(t2))
print(common)