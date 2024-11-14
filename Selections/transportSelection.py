#QUESTION: Choose a mode of transportation based on the distance. Example - <3km: walk, 3-15km: bike, >15km: car.

km = 17

if km < 3:
    mode = "Walk"
elif km <= 15:
    mode = "Bike"
else:
    mode = "Car"

print("Mode of transportation is",mode)