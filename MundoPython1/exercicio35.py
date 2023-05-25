a = int(input('Digite uma das retas:'))
b = int(input('Digite uma das retas:'))
c = int(input('Digite uma das retas:'))
if (a + b) > c:
    if (a + c) > b:
        if (b + c) > a:
            print('Elas podem formar um triangulo')
        else:
            print('Elas não podem formar um triangulo')
    else:
        print('Elas não podem formar um triangulo')
else:
    print('Elas não podem formar um triangulo')
#ou
#if a < b + c and b < a + c and c < a + b:
#   print('Elas podem formar um triangulo')
# else:
#   print('Elas não podem formar um triangulo')
