# Caso 1
x = range(10)
for i in x:
    print(i)

# Caso 2
x = range(10)
rta = "rango = |"
for i in x:
    rta = rta + str(i) + ", "
rta = rta + "|"
print(rta)

# Caso 3
x = range(3,10)
rta = "rango = |"
for i in x:
    rta = rta + str(i) + ", "
rta = rta + "|"
print(rta)

# Caso 4
x = range(3,10,2)
rta = "rango = |"
for i in x:
    rta = rta + str(i) + ", "
rta = rta + "|"
print(rta)