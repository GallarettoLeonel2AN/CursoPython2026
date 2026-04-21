nombre = input("Ingrese el nombre del jugador: ")

match nombre:
    case "Messi" | "Pique" | "Suarez":
        equipo = "Barcelona"
    case "Ronaldo" | "Benzema" | "Bale":
        equipo = "Real Madrid"
    case "Griezman" | "Koke" | "Godin":
        equipo = "Atetico Madrid"
    case _:
        equipo = "No se encontro equipo para el jugador"

if equipo != "No se encontro equipo para el jugador":
    print(f"{nombre} pertenece al equipo {equipo}")
else : print("El jugador no tiene equipo")
