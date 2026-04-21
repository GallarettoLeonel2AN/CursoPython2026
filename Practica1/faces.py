def Convert(texto):
   entrada = texto.replace(":)","😊").replace(":(","😞")
   return entrada

def main():
    texto= input("Escribe algo con emociones: ")
    entrada = Convert(texto)
    print(entrada)

main()