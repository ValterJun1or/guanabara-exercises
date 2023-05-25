num = int(input('Digite um número inteiro:'))
n = int(input('Digite até onde você quer que a tabuada vá:'))
for numero in range(1, n+1):
    print('{} x {} = {}'.format(num, numero, num * numero))
print('-------------------------------')
print('              Fim              ')
