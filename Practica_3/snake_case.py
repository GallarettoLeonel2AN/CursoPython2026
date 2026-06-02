
def main():
    camel = input("Ingresa una variable en camellCase: ")
    
    snake = ""

    for letra in camel:
        if letra.isupper():
            snake += "_" + letra.lower()
        else : snake += letra

    print(f"Variable en sanke_case {snake}")

main()