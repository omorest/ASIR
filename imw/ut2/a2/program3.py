import sys
nota = float(sys.argv[1])

if nota >= 0 and nota <= 10:

	if nota < 5:
		print("Suspenso")

	elif nota >= 5 and nota < 7:
		print("Aprobando")

	elif nota >= 7 and nota < 9:
		print("Notable")

	elif nota >= 9 and nota < 10:
		print("Sobresaliente")

	elif nota == 10:
		print("Matricula de honor")

else:
	print(nota, "es una nota no válida")