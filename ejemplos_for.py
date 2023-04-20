# Ejemplo 1
rta = "Salida = |"
for i in [1,2,3,4,5,6,7,8,9,10]:
    rta = rta + str(i) + ", "
rta = rta + "|"
print(rta)

# Ejemplo 2
for numero in [1,2,3,4,5,6,7,8,9,10]:
    print("UIS NO ES UNO...")

# Ejemplo 3
rta = "Salida = |"
for i in (1,2,3,4,5,6,7,8,9,10):
    rta = rta + str(i) + ", "
rta = rta + "|"
print(rta)

# Ejemplo 4
rta = "Salida = |"
for i in (1,11):
    rta = rta + str(i) + ", "
rta = rta + "|"
print(rta)

# Ejemplo 5
rta = "Salida = |"
for i in "UIS no es uno":
    rta = rta + str(i) + ", "
rta = rta + "|"
print(rta)

# Ejemplo 6
suma = 0
for i in range(1,11):
    suma = suma + i
print(f"La suma es: {suma}")

# Ejemplo 7
frase = input("Digite una frase: ")
vocales = "aeiouAEIOU"
numero_vocales = 0
for i in frase:
    if i in vocales:
        numero_vocales = numero_vocales + 1
print(f"En la frase hay {numero_vocales} vocales")