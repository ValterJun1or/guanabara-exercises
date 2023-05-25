valor = float(input('Digite o valor a ser pago pelo produto:'))
print('\033[1mAs opções de pagamento são:\033[0m\nA vista (10% de desconto)\nA vista no cartão (5% de desconto)')
print('Em até 2x no cartão (preço normal)\n3x ou mais no cartão (20% de juros)')
escolha = str(input('\033[1mEscreva a opção da condição de pagamento que você quer:\033[0m')).lower().strip()

if escolha == 'a vista':
    preço = valor - (valor * 0.1)
    print('Com \033[32mum desconto de 10%\033[0m o valor final será de R${}'.format(preço))
elif escolha == 'a vista no cartão':
    preço = valor - (valor * 0.05)
    print('Com \033[32mum desconto de 5%\033[0m o valor final será de R${}'.format(preço))
elif escolha == 'em até 2x no cartão':
    preço = valor
    print('Sem nenhum desconto o valor final será de R${}'.format(preço))
elif escolha == '3x ou mais no cartão':
    preço = valor + (valor * 0.2)
    print('Com \033[32m20% de juros\033[0m o valor final a ser pago será de R${}'.format(preço))
else:
    print('---     %       ---\033[31mERRO\033[0m---        %      ---')
    print('--------------------------------------------')
    print('Veja se não digitou errado alguma das opções')
    print('--------------------------------------------')
