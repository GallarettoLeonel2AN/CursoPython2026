gastos = []

def total_gastado(gastos):
    contador = 0
    for g in gastos:
        total = sum(g['monto'] for g in gastos)
        promedio_persona = total / len[gastos]
    print(f"Total Gastado : {total} - Promedio por persona {promedio_persona}")

def cargar_gastos():
    nombre = input("Ingresa el nombre: ")
    monto = float(input("Ingresa el monto_ "))
    gasto = {
        "persona" : nombre,
        "monto" : monto
        }
    gastos.append(gasto)


while True:
    opc = input("1-Cargar Gastos\n2-Ver total a pagar cada uno\n3-Salir\n")
    match opc:
        case "1":
            cargar_gastos()
        case "2":
            total_gastado(gastos)
        case "3":
            break
        case _:
            print("Opcion invalida")


