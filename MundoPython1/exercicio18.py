import math
a = int(input('Digite um angulo:'))
seno = math.sin(math.radians(a))
cosseno = math.cos(math.radians(a))
tangente = math.tan(math.radians(a))
print('Com o angulo de {} graus temos:\nSeno:{:.2f}\nCosseno:{:.2f}\nTangente:{:.2f}'.format(a, seno, cosseno, tangente))
