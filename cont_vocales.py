frase = input("Digite una frase: ")
na = "aáAÁ"
ne = "eéEÉ"
ni = "iíIÍ"
no = "oóOÓ"
nu = "uúUÚ"
ca = 0
ce = 0
ci = 0
co = 0
cu = 0
for i in frase:
    if i in na:
        ca += 1
    elif i in ne:
        ce += 1
    elif i in ni:
        ci += 1
    elif i in no:
        co += 1
    elif i in nu:
        cu += 1

print(f"En la frase hay {ca} letras a.")
print(f"En la frase hay {ce} letras e.")
print(f"En la frase hay {ci} letras i.")
print(f"En la frase hay {co} letras o.")
print(f"En la frase hay {cu} letras u.")