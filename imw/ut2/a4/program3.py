import sys

num = int(sys.argv[1])
texto = sys.argv[2]

if num > 0:
    texto_list = texto.split()

    suma = 0
    for i in texto_list:
        if len(i) == num:
            suma += 1
    print (f"Hay {suma} palabras de tamaño {num}")
else:
    print(f"Error: el número {num} es negativo!")
