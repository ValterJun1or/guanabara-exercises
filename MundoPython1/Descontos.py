p = float(input('Qual o preço do produto?'))
d = int(input('Qual o valor do desconto?'))
c = d / 100
D = p * c
np = p - D
print('Com um desconto de {}% o valor do produto será de {} reais'.format(d, np))