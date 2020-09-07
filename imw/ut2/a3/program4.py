import sys

n = int(sys.argv[1])

if n > 0:
    facto = 1
    for i in range(1, n + 1):
        facto = i * facto
        print("{}! = {}".format(i, facto))

else:
    print("Error: el número es negativo!")
