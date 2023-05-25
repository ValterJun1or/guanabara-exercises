num = int(input('Digite um número para saber se ele é primo:'))
conta = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[7:35m{}\033[0m'.format(c))
        conta += 1
    elif num % c != 0:
        print('\033[35m{}\033[0m'.format(c))

    if conta == 2 and c == num:
        print('Por ter \033[1:35m{}\033[0m números divisiveis ele é primo'.format(conta))
    elif conta != 2 and c == num:
        print('Por ter \033[1:35m{}\033[0m números divisiveis ele não é primo'.format(conta))
