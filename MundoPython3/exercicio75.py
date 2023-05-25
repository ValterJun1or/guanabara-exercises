cont_par = cont_9 = 0

num = (int(input("Digite o primeiro número:")),
       int(input("Digite o segundo número:")),
       int(input("Digite o terceiro número:")),
       int(input("Digite o quarto número:"))
       )

for numero in num:
    if (numero % 2) == 0:
        cont_par += 1
    if numero == 9:
        cont_9 += 1

print(f"Você digitos os valores:{num}")
print(f"Desses você digitou o número nove \033[35m{cont_9}\033[0m vezes e", end=" ")
if 3 in num:
    num_3 = (num.index(3))
    print(f"o primeiro três foi o \033[35m{(num_3 + 1)}º\033[0m número digitado, certo?")
else:
    print(f"o número três não foi digitado.")

print(f"Também percebi que dos quatro números \033[35m{cont_par}\033[0m são pares.")
