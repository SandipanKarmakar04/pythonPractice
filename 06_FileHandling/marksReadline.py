with open('marks.txt', 'r') as file:
    i = 0
    while True:
        i = i + 1
        l = file.readline()
        if not l:
            break
        m1 = int(l.split(",")[0])
        m2 = int(l.split(",")[1])
        m3 = int(l.split(",")[2])

        print(f"Marks in Maths of student {i}: {m1}")
        print(f"Marks in English of student {i}: {m2}")
        print(f"Marks in Computer of student {i}: {m3}\n")

