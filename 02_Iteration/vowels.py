# Taking input from the user
string = input("Enter a string: ")

# List of vowels
vowels = "aeiouAEIOU"
count = 0
# Print vowels found in the string
print("Vowels in the string:", end=" ")
for char in string:
    if char in vowels:
        print(char, end=" ")
        count = count + 1
print("\ntotal vowels are: " ,str(count))
