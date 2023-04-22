# 3. Simular el lanzamiento de N dados o de un dado N veces, e imprimir cuántas veces cayó cada cara. Mostrar el resultado con barra de asterisco.
# Ejercicio No. 46: Dados.

from random import randint

c1 = ""
c2 = ""
c3 = ""
c4 = ""
c5 = ""
c6 = ""
n1 = 0
n2 = 0
n3 = 0
n4 = 0
n5 = 0
n6 = 0


n = int(input("¿Cuántas veces se va a lanzar el dado?: "))

for i in range(n):
    cara = randint(1, 6)
    if cara == 1:
        c1 += "*"
        n1 += 1
    elif cara == 2:
        c2 += "*"
        n2 += 1
    elif cara == 3:
        c3 += "*"
        n3 += 1
    elif cara == 4:
        c4 += "*"
        n4 += 1
    elif cara == 5:
        c5 += "*"
        n5 += 1
    elif cara == 6:
        c6 += "*"
        n6 += 1

print("Resultados")
print("El número 1 salió",n1,"veces:", c1)
print("El número 2 salió",n2,"veces:", c2)
print("El número 3 salió",n3,"veces:", c3)
print("El número 4 salió",n4,"veces:", c4)
print("El número 5 salió",n5,"veces:", c5)
print("El número 6 salió",n6,"veces:", c6)