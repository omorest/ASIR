import random

NUCLEOBASES = "ATGC"
DNA_SIZE = 100

sequence = "".join([random.choice(NUCLEOBASES) for i in range(DNA_SIZE)])

a = 0
t = 0
g = 0
c = 0

for char in sequence:
    if char == "A":
        a += 1
    elif char == "T":
        t += 1
    elif char == "G":
        g += 1
    elif char == "C":
        c += 1
print(f"Adenine = {a}\nThymine = {t}\nCytosine = {c}\nGuanine = {g}")
