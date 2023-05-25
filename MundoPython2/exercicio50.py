s = 0
c = 0
for n in range(1, 7):
    num = int(input('Digite um número inteiro:'))
    if num % 2 == 0:
        s += num
        c += 1
print('A soma dos {} números pares digitados é igual a {}'.format(c, s))
