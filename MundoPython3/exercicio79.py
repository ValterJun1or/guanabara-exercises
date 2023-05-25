lista = []
res = "s"
num = 0

while res in 's sim S SIM sim':
    num = int(input("Digite um número:"))
    if num not in lista:
        lista.append(num)
    else:
        print(f"O número {num} já foi colocado.")
    res = str(input('Deseja adicionar mais algum número?'))
lista.sort()
print(f"Você digitou {lista}")
