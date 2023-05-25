from time import sleep

n1 = float(input('Digite um número:'))
n2 = float(input('Digite outro número:'))

escolha = 0

print('[1]somar números\n'
      '[2]Multiplicar números\n'
      '[3]O maior número\n'
      '[4]Colocar outros números\n'
      '[5]Sair do programa\n')

while escolha != 5:
    escolha = int(input('Digite uma das opções acima:'))
    if escolha == 1:
        soma = n1 + n2
        print('A soma de {} e {} é igual a {}'.format(n1, n2, soma))
    elif escolha == 2:
        multipli = n1 * n2
        print('A multiplicação entre {} e {} é igual a {:.2f}'.format(n1, n2, multipli))
    elif escolha == 3:
        if n1 > n2:
            print('{} é maior que {}'.format(n1, n2))
        elif n2 > n1:
            print('{} é maior que {}'.format(n2, n1))
        elif n1 == n2:
            print('{} e {} são iguais'.format(n1, n2))
    elif escolha == 4:
        n1 = float(input('Digite um número \033[35mnovamente:\033[m'))
        n2 = float(input('Digite outro número \033[35mnovamente\033[m:'))
    elif escolha == 5:
        print('.', end=' ')
        sleep(1)
        print('.', end=' ')
        sleep(1)
        print('.')
        sleep(1)
    else:
        print('Você digitou errado.')

print('\033[1mVocê saiu do programa.')
