frase = str(input('Digite um frase para saber se ela é um polindromo:')).lower()
frase2_0 = frase.split()
junto = ''.join(frase2_0)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Essa frase é um palíndromo')
else:
    print('Essa frase não é um palíndromo')
'''OU
frase = str(input('Digite um frase para saber se ela é um polindromo:')).lower()
frase2_0 = frase.split()
junto = ''.join(frase2_0)
inverso = junto[::-1]
if inverso == junto:
    print('Essa frase é um palíndromo')
else:
    print('Essa frase não é um palíndromo')'''
