lista = []
quant = 0

while True:
    n = int(input('Digite um número:'))
    lista.append(n)
    quant += 1
    per = str(input("Deseja digitar outro número?[S/N]"))
    if per in 'Nn não NÃO Não':
        break

lista.sort(reverse=True)
print(f"Você digitou {quant} valores.")
print(f'A lista em ordem decrescente:{lista}.')
if 5 in lista:
    print("O 5 está na lista.")
else:
    print("O 5 não está na lista.")
