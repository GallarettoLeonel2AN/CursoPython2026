datos = []
def v_dni():
    while True:
        dni = input("Ingresa el dni: ").strip()
        if  dni.isdigit() and (len(dni) == 8 or len(dni) == 7):
            return dni
        else:
            print("ingresar solo numeros")
            

def es_valido(nombre,dni):
    dato = {
    "Nombre_Completo" : nombre,
    "Dni": dni
     }
    datos.append(dato)
    print("Datos cargados correcatamente")
    print("DNI valido")
    return True
        
def ver_datos():
     if not datos:
            print("No hay nada que mostrar")
            return
     else:
         for u in datos:
           print(f"Nombre : {u['Nombre_Completo']} - Dni: {u['Dni']}")
            
while True:
    opc = input("1-Cargar Datos \n2-Ver Datos \n3-Salir")
    match opc:
        case "1":
            nombre = input("ingresa nombre y apellido: ").title().strip()
            udni = v_dni()
            es_valido(nombre,udni)
        case "2":
            ver_datos()
        case "3":
            break
        case _:
            print("opcion invalida")