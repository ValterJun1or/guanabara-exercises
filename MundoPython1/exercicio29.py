v = int(input('Digite a velocidade do veiculo em km/h:'))
print('A velocidade do veiculo foi {}km/h'.format(v))
if v > 80:
    print('O veiculo foi multado!!!')
    m = v - 80
    f = m * 7
    print('Com um excesso de {}km/h a multa a ser paga será de R${:.2f}'.format(m, f))
else:
    print('O veiculo não foi multado.')
    print('Ele não terá que pagar nenhuma multa.')
