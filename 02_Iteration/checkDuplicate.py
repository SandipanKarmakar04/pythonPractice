items = ["apple", "banana", "orange", "apple", "mango"]
unique = set()

for item in items:
    if item in unique:
        print("duplicate",item)
        break
    else:
        unique.add(item)