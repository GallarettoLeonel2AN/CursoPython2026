
nombre = input("Ingrese su nombre: ")
mail = input("Ingrese su Correo: ")

nombre = nombre.strip().title()
mail = mail.strip()

usuario = {
     "nombre": nombre,
     "mail": mail
    }

# Grupo 3

def depositar(saldo):
    cantidad = float((input("Ingresa la cantidad a Depositar: $")))
    if cantidad > 0:
        saldo+=cantidad
    else: 
        print("Saldo Invalido")
    print(f"Su saldo actual es {saldo}")
    return saldo

def extraer(saldo):
    cantidad = float((input("Ingresa la cantidad a Extraer: $")))
    if cantidad > 0 and cantidad <= saldo:
        saldo-=cantidad
    else: 
        print("Saldo insuficiente")
    print(f"Su saldo actual es {saldo}")
    return saldo
# Grupo 2
saldo = 0.0;
while True:
    opcion = input("elige una opcion\n 1:Depositar\n 2:Extraer\n 3:Historial\n 4:Salir\n")
    match opcion:
        case "1":
            saldo = depositar(saldo)
        case "2":
            saldo = extraer(saldo)
        case "3":
            print("")
        case "4":
            break   
        case _:
            print("Opcion Invalida")

