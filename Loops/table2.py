#QUESTION: Print the mumtiplication table but skip the 5th iteration.
n = int(input("enter the value: "))

multi= 0


for i in range(1, 10+1):
    multi = n*i
    if i == 5:
        continue
    print(n,"X",i,"=",multi)