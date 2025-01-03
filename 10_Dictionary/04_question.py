d = {"ethan":97, "jade":90, "victor":95}

top = max(d, key=d.get)
print(top, d[top])