import sys

n = int(sys.argv[1])

if n > 0:
    suma = 0
    for i in range(1, n + 1):
        j = i ** 2
        suma = j + suma
    else:
        print(suma)
else:
    print("Error: el numero", n, " es negativo!")
