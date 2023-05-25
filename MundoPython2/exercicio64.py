numero = int(input("Digite um número(999 para parar):"))
cont = total = 0
while numero != 999:
    cont += 1
    total += numero
    numero = int(input("Digite um número(999 para parar):"))
print(f"A soma dos números digitados foi igual á \033[36m{total}\033[0m")
print(f"\033[34m{cont}\033[0m números foram digitados.")
