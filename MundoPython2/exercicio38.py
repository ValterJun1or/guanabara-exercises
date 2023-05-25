n1 = float(input('Digite um numero:'))
n2 = float(input('Digite outro numero:'))
Z = '---' * 3

if n1 > n2:
    print('O primeiro numero é maior que o segundo numero.')
elif n2 > n1:
    print('O segundo numero é maior que o primeiro numero.')
elif n1 == n2:
    print('Os numeros tem o mesmo valor.')
else:
    print('{}\033[31m ERRO \033[0m{}'.format(Z, Z))
