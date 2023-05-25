a = int(input('Digite uma das retas:'))
b = int(input('Digite uma das retas:'))
c = int(input('Digite uma das retas:'))

if a < b + c and b < a + c and c < a + b:
   print('Elas podem formar um triangulo')
   if a != b != c:
      print('O triangulo é escaleno')
   elif a == b == c:
      print('O triangulo é equilátero')
   elif a == b and a != c or a == c and a != b or b == c and a != c:
      print('O triangulo é isósceles')
else:
   print('Elas não podem formar um triangulo')
