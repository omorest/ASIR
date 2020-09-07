import sys

n = int(sys.argv[1])

if n > 0:
    for i in range(2, n):
        resto = n % i
        if resto == 0:
            print ("El número", n, "no es primo!")
            break
    else:
        print("El numero", n, "es primo!")
else:
    print("Error: el número", n, "es negativo!")
