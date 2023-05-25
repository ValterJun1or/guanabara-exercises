d = float(input('Digite a distancia da viagem em km:'))
if d <= 200:
    c = d * 0.50
    print('O preço da passagem será de R${:.2f}'.format(c))
else:
    c = d * 0.45
    print('O preço da passagem será de R${:.2f}'.format(c))
