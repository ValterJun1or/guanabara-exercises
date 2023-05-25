s = int(input('Digite seu salário:'))
a = int(input('Digite a porcentagem do seu aumento:'))
sp = a / 100
st = s * sp
sd = s + st
print('Seu salário atual é de {:.2f}R$,com {}% de aumento seu novo salário será de {:.2f}R$'.format(s, a, sd))