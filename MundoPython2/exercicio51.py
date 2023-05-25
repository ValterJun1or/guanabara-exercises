p = int(input('Digite o primeiro termo inteiro da sua progressão aritmétrica:'))
r = int(input('Digite a razão da sua progressão aritmétrica:'))
f = p + (10 - 1) * r
for pa in range(p, f + r, r):
    print(pa)
print('Fim')