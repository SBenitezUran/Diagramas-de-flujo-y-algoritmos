# Para determinar si un número es negativo o positivo.
num = float(input("introduce un número:"))
if num > 0:
  print("El número es positivo.")
else:
  print("El número es negativo.")

# Actividad 1:
# Mayor o menor de edad.
num = float(input("introduzca su edad:"))
if num >= 18:
  print("Es mayor de edad.")
else:
  print("Es menor de edad.")
  
# Actividad 2:
# Número entero.
while True:
    try:
        numero = int(input("por favor ingrese un número entero: "))
        break
    except ValueError:
        print("Lo siento, no ingresaste un número entero. Intente nuevamente.")

print("el número que ingresó es:", numero)

# Número par
num = float(input("ingrese un número:"))
if num % 2 == 0:
  print("El número es par")
else:
  ("No es un número par")
  