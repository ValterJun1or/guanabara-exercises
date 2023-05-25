n = int(input('Digite um número inteiro:'))
print('''
1 = binário
2 = octal
3 = hexadecimal
''')
escolha = int(input('\033[35mDigite qual opção você deseja escolher:\033[0m'))

if escolha == 1:
    print('O número {} traduzido em \033[34mbinário\033[0m fica igual a {}'.format(n, bin(n)[2:]))
elif escolha == 2:
    print('O número {} traduzido em \033[34moctal\033[0m fica igual a {}'.format(n, oct(n)[2:]))
elif escolha == 3:
    print('O número {} traduzido em \033[34mhexadecimal\033[0m fica igual a {}'.format(n, hex(n)[2:]))
else:
    print('\033[32mAlgo deu errado,verifique se digitou de forma correta.\033[0m')