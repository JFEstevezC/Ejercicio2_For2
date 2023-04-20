# Leer N numeros enteros (uno en cada lectura), mostrar e imprimir cuantos son pares y cuantos son impares.

pares = 0
impares = 0

n = int(input("Ingrese la cantidad de números que desea ingresar"))

for i in range(n):
    m = int(input("Ingrese un valor: "))
    c = m % 2
    if c == 0:
        pares += 1
    else:
        impares += 1
print(f"El número de pares es: {pares}. Y el número de impares es: {impares}")
