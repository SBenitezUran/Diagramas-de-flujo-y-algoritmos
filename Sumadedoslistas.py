"""Crear un programa que reciba dos listas de números y
que genere una tercera lista que contenga la suma de
los elementos de las dos listas en la misma posición,
utilizando un ciclo for"""


# Ingreso de listas
lista1 = [int(num) for num in input("Ingrese la primera lista de números separados por espacios: ").split()]
lista2 = [int(num) for num in input("Ingrese la segunda lista de números separados por espacios: ").split()]

# Verificación de longitudes de listas
if len(lista1) != len(lista2):
    print("Las listas deben tener la misma cantidad de elementos.")
else:
    lista3 = []
    # Suma de elementos en la misma posición
    for i in range(len(lista1)):
        lista3.append(lista1[i] + lista2[i])
    # Impresión de lista resultante
    print("La lista resultante es: ", lista3)

    