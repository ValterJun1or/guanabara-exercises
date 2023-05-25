import random
from time import sleep
dicionario = {'pedra': '1', 'papel': '2', 'tesoura': '3'}
p = 'pedra'
pa = 'papel'
t = 'tesoura'
escolha = str(input('Escolha pedra,papel ou tesoura:')).lower().strip()
computador = str(random.randint(1, 3))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print("Dicionário:Pedra = 1 / papel = 2/ tesoura = 3")
print('O computador escolheu \033[35m{}'.format(computador))

if escolha == p and computador == '3' or escolha == pa and computador == '1' or escolha == t and computador == '2':
    print('Voce ganhou!!!')

elif escolha == t and computador == '1' or escolha == p and computador == '2':
    print('Voce perdeu.')
elif escolha == pa and computador == '3':
    print('Voce perdeu.')

elif escolha == p and computador == '1' or escolha == pa and computador == '2':
    print('Voces empataram.')
elif escolha == t and computador == '3':
    print('Voces empataram.')

else:
    print('Erro no procedimento,veja se voce não digitou umas das três opções de forma errada')
