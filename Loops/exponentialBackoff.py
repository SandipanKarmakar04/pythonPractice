import time

waitTime = 1
maxTries = 5
attempts = 0

while attempts < maxTries:
    print("Attempt", attempts + 1,"wait time",waitTime,"second")
    time.sleep(waitTime)
    waitTime *= 2
    attempts += 1