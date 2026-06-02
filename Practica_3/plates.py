
def main():
    while True:
        plate = input("Ingrese Placa: ").strip()
        
        if plate.lower() == "salir":
           break
        else :
            if es_valida(plate):
                print("Es Valida")
            else : print("Placa invalida")

def es_valida(s):
    
    if not (6 >= len(s) >= 2):
        return False  
    
    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    if not s.isalnum():
        return False

    for i in range(len(s)):
        if s[i].isdigit():
            if s[i] == "0":
                return False

            if not s[i:].isdigit():
                return False
            break
    
    return True

main()