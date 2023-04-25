# mi rutina diaria.
print("¿Madrugar o no?")
decisión = input ("Escriba 'si o 'no':")

#si la respuesta es "no"
if decisión == "no":
    print("No me rinde el día, no alcanzo a realizar todas mis tareas. No tendré un día productivo.")
    exit()
#si la respuesta es "si"
if decisión == "si":
    print("¿ir al gym, hacer trabajos o hacer ambos?")
    que_hacer = input ("Escriba 'gym' o ' trabajos' o 'ambos':")
    if que_hacer == "gym":
        print("Si no tengo trabajos pendientes puedo ir")
        exit()
    elif que_hacer == "trabajos":
        print("Si tengo muchos trabajos pendientes")
        exit()
    elif que_hacer == "ambos":
        print("Si tengo tiempo para realizar ambas actividades")
        exit()