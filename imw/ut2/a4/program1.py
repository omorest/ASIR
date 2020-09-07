import sys

n_dni = sys.argv[1]
letras = "TRWAGMYFPDXBNJZSQVHLCKE"

if len(n_dni) == 8:
    n_dni = int(n_dni)
    n_letra = n_dni % 23
    l_dni = letras[n_letra]
    print(f"{n_dni}{l_dni}")
else:
    print("Error: el número del dni tienen que ser 8 digitos!")
