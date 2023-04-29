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
  print("El número es par.")
else:
  print("No es un número par.")