from math import sqrt

import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

if a == 0:
	print("X = ", -c / b)

elif (b ** 2 - 4 * a * c) < 0:
	print("La ecuacion no tiene solución real")

else: 
	print("X1 = ", (-b + sqrt(b ** 2 - 4 * a * c)) / (2 * a))
	print("X2 = ", (-b - sqrt(b ** 2 - 4 * a * c)) / (2 * a))
