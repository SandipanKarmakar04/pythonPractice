#QUESTION: Movie tickets are priced base on age. $12 for adults(18 and over), $8 for children. Everyone gets a $2 discount on wednesday.

age = 6
day = "Wednesday"

price = 12 if age >= 18 else 8

if day == "Wednesday":
    price = price - 2
    # price -= 2

print("Ticket price for you is $",price)