#QUESTION: Calculate the sum of even numbers up to given number N.
n = 10

sumEven = 0

for i in range(1, n+1):
    if i%2 == 0:
        sumEven += i


print("Sum of even number is:",sumEven)