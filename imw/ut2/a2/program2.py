from math import sqrt

import sys

x1 = float(sys.argv[1])
y1 = float(sys.argv[2])

x2 = float(sys.argv[3])
y2 = float(sys.argv[4])

x3 = float(sys.argv[5])
y3 = float(sys.argv[6])


dis_punto2 = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

dis_punto3 = sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)


# Comparación
if dis_punto3 < dis_punto2:
	print("El punto más cercano a (", x1, ",", y1, ") es (", x3, ",", y3, ") y está a una distancia de :", dis_punto3)

elif dis_punto2 < dis_punto3:
	print("El punto más cercano a (", x1, ",", y1, ") es (", x2, ",", y2, ") y está a una distancia de :", dis_punto2)