import sys
num = sys.argv[1:]
cant_num = len(num)

suma = 0
for i in num:
    i = float(i)
    suma += i
result = suma / cant_num
print(f"La media de los valores es: {result}")
