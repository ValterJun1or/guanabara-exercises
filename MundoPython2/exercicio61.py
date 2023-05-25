primeiro = int(input('Digite o primeiro termo da sua progressão aritmétrica:'))
razao = int(input('Digite a razão da sua progressão aritmétrica:'))
termo = primeiro
cont = 1

while cont <= 10:
    print(f'{termo}, ' if cont <= 9 else f'{termo}.', end='')
    termo += razao
    cont += 1
print("\nFim.")