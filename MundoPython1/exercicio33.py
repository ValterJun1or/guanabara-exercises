a = float(input('Digite um numero:'))
b = float(input('Digite outro numero:'))
c = float(input('Digite um terceiro numero:'))
if a > b and a > c:
    print('O maior numero é {}'.format(a))
else:
    if b > a and b > c:
        print('O maior número é {}'.format(b))
    else:
        if c > a and c > b:
            print('O maior numero é {}'.format(c))
        else:
            ('---ERRO---')
if a < b and a < c:
    print('O menor numero é', a)
else:
    if b < c and b < a:
        print('O menor numero é', b)
    else:
        if c < a and c < b:
            print('O menor numero é', c)
        else:
            print('---ERRO---')

