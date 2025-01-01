inputStr = "teetery"

for char in inputStr:
    if inputStr.count(char) == 1:
        print("Non-repeated character is:",char)
        break