import random
n = random.randint(0, 10)
resposta = int(input('Adivinhe o número que o computador pensou:'))
erros = 0

while n != resposta:
    resposta = int(input('\033[31mVocê errou\033[0m \nTente novamente:'))
    erros += 1

print('\033[32mCERTO!!!\033[m')
print('Após {} erros você acertou,parábens.'.format(erros))
