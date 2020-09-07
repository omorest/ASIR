import sys
moneda=int(sys.argv[1])

billetes_50 = moneda // 50


if billetes_50 > 0:
    print (moneda // 50, "billetes de 50")
        
    resto = moneda % 50
billetes_20 = resto // 20
        
if billetes_20 > 0:
    print (resto // 20, "billetes de 20")
        
    resto = resto % 20
billetes_10 = resto // 10
        
if billetes_10 > 0:
    print (resto // 10, "billetes de 10")
        
    resto = resto % 10
billetes_5 = resto // 5
        
if billetes_5 > 0:
    print (resto // 5, "billetes de 5")
        
    resto = resto % 5
monedas_2 = resto // 2
    
if monedas_2 > 0:
    print (resto // 2, "monedas de 2")
        
    resto = resto % 1
monedas_1 = resto // 1
        
if monedas_1 > 0:
    print (resto // 1, "monedas de 1")
        
    resto = resto % 1
