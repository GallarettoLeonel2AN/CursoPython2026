respuesta = input("Ingresa el numero operacion numero ")

x,y,z = respuesta.split(" ")

x = float(x)
z = float(z)

match y :
    case y if y == "+":
        resultado = x + z
    case y if y == "-":
        resultado = x - z
    case y if y == "*":
        resultado = x * z
    case y if y == "/":
        resultado = x / z
    case _: 
        print("nada")
        
print(resultado)        