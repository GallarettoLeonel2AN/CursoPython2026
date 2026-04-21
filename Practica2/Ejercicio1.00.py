numero = int(input("Escriba el numero que quiera: "))

match numero:
        case n if n < 0:
            print ("El numero es Negativo")
        case n if n > 0:
            print ("El numero es Positivo")
        case _:
            print ("El numero es Cero")