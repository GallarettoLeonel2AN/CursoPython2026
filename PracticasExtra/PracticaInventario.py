inventario = []

def agregar_producto(nombre,cantidad,precio):
    
    producto = {
        "nombre" : nombre,
        "cantidad" : cantidad,
        "precio" : precio
        }
    inventario.append(producto)

def lista_productos():
    for pro in inventario:
        total_producto = pro['cantidad'] * pro['precio']
        print(f"{pro['nombre']}\n :Total ${total_producto:.2f}")

def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Entrada invalida. Por favor, ingrese un numero entero.")
while True:
    opcion = input("1-Cargar Producto\n2-Ver Productos\n3-Salir\n ")    
    match opcion:
        case "1":
            try:
                nombre = input("Nombre Producto: ").strip().lower()
                cantidad = leer_entero("cantidad: ")
                precio = float(input("Precio: "))
                agregar_producto(nombre,cantidad,precio)
                print("producto agregado con exito")
            except ValueError:
                print("Solo se permiten numeros")
        case "2":
            lista_productos()
        case "3":
            break
        case _:
            print("Invalido")


