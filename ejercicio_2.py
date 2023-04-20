# Mostar e imprimir cuantos múltiplos de 7 y cuántos múltiplos de 9 hay entre 1000 y 5000.
m7=0
m9=0
for i in range(1000,5000):
    a = i % 7
    b = i % 9
    if a == 0:
        m7 = m7 + 1
    if b == 0:
        m9 = m9 + 1
print(f"El número de múltiplos de 7 del 1000 al 5000 es: {m7}")
print(f"El número de múltiplos de 9 del 1000 al 5000 es: {m9}")