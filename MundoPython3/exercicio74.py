from random import randint

cont = maior = menor = 0
ale = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))

print("Esses são os números da lista:")
print('-=-' * 25)
while True:
    num = ale[cont]
    print(num)
    if cont == 0:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    cont += 1
    if cont > 4:
        break
print('-=-' * 25)
print(f'Entre eles o maior foi {maior} e o menor {menor}')
# OU #
# Ao invés de maior e menor o comando max(ale) e min(ale) trazem o mesmo resultado de uma forma mais simples
print(f'Entre eles o maior foi {max(ale)} e o menor {min(ale)}')
