def main():
    while True:
        try:
            fraccion = input("Ingresa la fraccion en x/y ").strip()
            fraccion = fraccion.split("/")
            x = int(fraccion[0])
            y = int(fraccion[1])
            if x > y : continue
            porcentaje =  round((x/y) * 100)
            
            match porcentaje:
                case porcentaje if porcentaje <= 1:
                    print("E")
                case porcentaje if porcentaje >= 99:
                    print("F")
                case _:
                    print(f"% {porcentaje}")
            break
        except (ValueError,ZeroDivisionError,IndexError) :
        
            pass
main()