def main() :
    hora = input("Ingresa la hora en formato ##:## ")
    hora = convert(hora)

    match hora:
        case hora if  7.00 <=  hora <= 8.00:
            print("hora de desayunar")
        case hora if  12.00 <=  hora <= 13.00:
            print("hora de almorzar")
        case hora if  18.00 <=  hora <= 19.00:
            print("hora de cenar")



def convert(hora):
    horas,minutos = hora.split(":")
    horas = float(horas)
    minutos = float(minutos)
    return horas + (minutos / 60)

main()