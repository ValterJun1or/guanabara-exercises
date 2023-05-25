p = float(input('Qual o preço do produto?'))
di = float(input('Qual o percentual de desconto?'))
d = di / 100
df = p * d
np = p - df
print('Com um desconto de {}% o valor final será de {}'.format(df, np))
