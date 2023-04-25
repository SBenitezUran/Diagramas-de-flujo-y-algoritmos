# Bienvenidos a la isla, tu misión será encontrar el tesoro:
print("¿Por dónde empezarás?")
direccion = input("Escriba 'izquierda' o 'abajo' o 'derecha':")

# Si la respuesta es 'izquierda' entonces:
if direccion == "izquierda":
    print("te encuntras un leon")
    print("¿correr o pelear?")
    que_hacer = input("Escriba 'correr' o 'pelear':")
    if que_hacer == "correr":
        print("muerte desesperada")
    elif que_hacer == "pelear":
        print("muerte de un valiente")
        exit()
if direccion == "derecha":
    print("caiste en un agujero, GAME OVER")
    exit()
if direccion == "abajo":
    print("caes a un lago")
    print("¿nadar o esperar?")
    que_hago = input("Escriba 'nadar' o 'esperar':")
    if que_hago == "nadar":
        print("te encuentras 3 barcos")
        cual_elijo = input("Escriba 'azul' o 'rojo' o 'negro':")
        if cual_elijo == "azul":
            print("te disparan, GAME OVER")
        elif cual_elijo == "negra":
             print("devorado por las culebras, GAME OVER")
        elif cual_elijo == "rojo":
            print("te rescatan, GANASTE")
    elif que_hago == "esperar":
        print("mueres ahogado o devorado por las pirañas")
        
    


   
    
    
   
    
