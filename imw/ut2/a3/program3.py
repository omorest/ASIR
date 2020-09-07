import sys

n1 = int(sys.argv[1])
n2 = int(sys.argv[2])

if n1 > 0 and n2 > 0:
    if n1 < n2:
        min = n1
        max = n2
    else:
        min = n2
        max = n1

    for i in range(min, 1 - 1, -1):
        if min % i == 0:
            if max % i == 0:
                print("El MCD de {} y {} es: {}".format(n1, n2, i))
                break
else:
    print("Error: Algún número es negativo!")
