print('\033[35m Peça  seu emprestimo aqui!!! \033[0m')
valor_casa = float(input("Digite o valor da casa:"))
salario = float(input('Digte seu salário:'))
anos = int(input('Digite a quantidade de tempo que você irá pagar a casa em anos:'))

prestacao_mensal = valor_casa / (anos * 12)
p = salario * 0.3

if prestacao_mensal > p:
    print('Sua prestação mensal será de R${:.2f}'.format(prestacao_mensal))
    print('\033[4:31m Seu emprestimo foi negado. \033[0m')
elif prestacao_mensal <= p:
    print('Sua prestação mensal será de R${:.2f}'.format(prestacao_mensal))
    print('\033[32m Seu emprestimo foi aprovado. \033[0m')
