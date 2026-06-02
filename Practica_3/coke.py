deuda = 50
while True:
    
    vuelto = 0
    try:
        moneda = int(input("Ingresa una moneda de 25c , 10c , 5c: "))
        match moneda:
            case 25:
                deuda -= moneda
                if deuda > 0:    
                    print(f"Falta saldar {deuda}")
                else:
                    vuelto = deuda * -1
                    print(f"Su vuelto es de {vuelto}")
                    break
            case 10:
                deuda -= moneda
                if deuda > 0:
                    
                    print(f"Falta saldar {deuda}")
                else:
                    vuelto = deuda * -1
                    print(f"Su vuelto es de {vuelto}")
                    break
            case 5:
                deuda -= moneda
                if deuda > 0:
                    print(f"Falta saldar {deuda}")
                else:
                    vuelto = deuda * -1
                    print(f"Su vuelto es de {vuelto}")
                    break
            case _:
                print(f"Moneda de valor no aceptado - Deuda: {deuda}")
    except ValueError :
        print("Solo Numeros")
       