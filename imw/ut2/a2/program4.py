import math

import sys
radio = float(sys.argv[1])


if radio >= 0:
	print("Menu (1), calcula el diámetro de la circunferencia. ")
	print("menú (2), calcula el perímetro de la circunferencia.")
	print("Menú (3), calcula el área del círculo.")
	print("Menú (4), sale del programa")

option_menu = int(input("¿Que opción del menú desea? : "))

if option_menu >= 1 and option_menu <= 4:
	if option_menu == 1:
		print("Diámetro = ", 2 * radio)

	if option_menu == 2:
		print("Perímetro = ", 2 * math.pi * radio)

	if option_menu == 3:
		print("Área = ", math.pi * radio ** 2)

	if option_menu == 4:
		sys.exit()
		print("Salir del menú")

else:
	print("Número de menú no válido")