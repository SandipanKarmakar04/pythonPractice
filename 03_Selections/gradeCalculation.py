#QUESTION: Assign a letter grade based on a student's score: A(90-100), B(80-89), C(70-79), D(60-69), F(Below 60)

score = 105

if score > 100:
    print("PLease verify your grade again.")
    exit()
elif score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print("Grade:",grade)