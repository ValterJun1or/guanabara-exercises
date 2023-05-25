media = 0
iv = 0
nv = ''
nm = 0
for c in range(1, 5):
    print('\033[1m{}ª pessoa\033[0m'.format(c))
    nome = str(input('Nome:'))
    idade = int(input('Idade:'))
    sexo = str(input('sexo(M ou F):')).strip().upper()
    media += idade
    if c == 1 and sexo in 'M':
        iv = idade
        nv = nome
    elif iv < idade and sexo in 'M':
        iv = idade
        nv = nome
    elif sexo in 'F' and idade < 20:
        nm += 1
print('A média da idade dos quatro é de {} anos'.format(media / 4))
print('O homem mais velho tem {} anos e se chama {}'.format(iv, nv))
print('Tem {} mulheres com menos de 20 anos'.format(nm))
