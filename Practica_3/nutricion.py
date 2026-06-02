def main():
    
    frutas = {
        "Apple": 130 , 
        "Avocado": 50 ,
        "Banana": 110 ,
        "Cantaloupe": 50 ,
        "Grapefruit": 60 ,
        "Grapes": 90 ,
        "HoneydewMelon": 50 , 
        "Kiwifruit": 90 ,
        "Lemon": 15 ,
        "Lime": 20 ,
        "Nectarine": 60 ,
        "Orange": 80 ,
        "Peach": 60 , 
        "Pear": 100 ,
        "Pineapple": 50 ,
        "Plums": 70 , 
        "Strawberries": 50 ,
        "SweetCherries": 100 ,
        "Tangerine": 50 ,
        "Watermelon": 80
    }
   
    fruta = input("Ingresa una Fruta: ").strip().lower()
    fruta = fruta.capitalize()
    print(fruta)
    def calorias(fruta):
       
       if fruta in frutas:
          print(f"Valor Nutricional {frutas[fruta]}")
          
            
    calorias(fruta)
main()
