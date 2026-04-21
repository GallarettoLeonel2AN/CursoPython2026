numero = int(input("Escriba su edad: "))

match numero:
        case n if n < 21:
            print ("Sos menor de edad")
        case n if n > 21 and n < 60:
            print ("Sos mayor de edad")
        case n if n > 21:
            print ("Sos jubilado")