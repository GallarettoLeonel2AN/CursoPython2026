
def es_vocal(letra):
    letra = letra.lower()
    return letra in "aeiou"

completa = input("Ingrese una palabra: ").strip()
corta = ""

for letra in completa:
    if es_vocal(letra):
        corta = corta
    else:
        corta += letra

print(corta)
        





    