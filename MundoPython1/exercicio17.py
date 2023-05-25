'''from math import sqrt
co = float(input('Digite o cateto oposto do triangulo retangulo:'))
ca = float(input('Digite o cateto adjacente do triangulo retangulo:'))
cu = (ca ** 2 + co ** 2)
h = sqrt(cu)
print('A hipotenusa do triangulo é {:.2f}'.format(h))'''
import math
co = float(input('Digite o cateto oposto:'))
ca = float(input('Digite o cateto adjacente:'))
h = math.hypot(co, ca)
print('A hipotenusa do triangulo retangulo é {:.2f}'.format(h))