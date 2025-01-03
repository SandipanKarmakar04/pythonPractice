# Flatten a nested list nested = [[1, 2, 3], [4, 5], [6, 7, 8]] into a single list.

nested = [[1, 2, 3], [4, 5], [6, 7, 8]]
flattened = [item for sublist in nested for item in sublist]

print(flattened)