def Main():
    dollar = dollars_to_float(input("Escriba el valor dela comida: "))    
    percent = percent_to_float(input("que porcentaje de propina desea dejar "))
    tip = dollar * percent
    print(f"Usted dejo de propina $ {tip:.2f}")



def dollars_to_float(entrada):
   r =  float(entrada)
   return r 

def percent_to_float(entrada):
    r = float(entrada)/100
    return r
Main()