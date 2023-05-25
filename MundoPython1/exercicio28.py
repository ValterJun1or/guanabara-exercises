import random
import time
n = random.randint(0,5)
r = int(input('Digite o numero que foi escolhido pela maquina:'))
print('*tambores*')
time.sleep(3)
print("O número escolhido pela maquina foi {}".format(n))
if n == r:
    print('Parabens,você acertou!!!')
else:
    print('Errastes papai,foi de comes e bebes!!!')
print('FIM')
