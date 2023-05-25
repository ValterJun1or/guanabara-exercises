print("Digite vários números,se quiser parar digite 999")
numero = int(input("Digite um número:"))
cont = total = 0
while True:
    if numero == 999:
        break
    cont += 1
    total += numero
    numero = int(input("Digite um múmero:"))
print(f"A soma dos números digitados foi igual á \033[36m{total}\033[0m")
print(f"\033[34m{cont}\033[0m números foram digitados.")
