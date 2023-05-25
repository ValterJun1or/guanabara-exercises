m = 0
n = 0
for peso in range(1, 6):
    p = float(input('Digite o peso da {}ª pessoa:'.format(peso)))
    if peso == 1:
        m = p
        n = p
    else:
        if p > m:
            m = p
        elif p < n:
            n = p
print('O maior peso é de {}Kg e'.format(m), end=' ')
print('o menor peso é de {}Kg'.format(n))
