n1 = float(input('Digite suas notas:\n'))
n2 = float(input(''))
media = (n1 + n2) / 2

if media < 5:
    print('\031[31m Reprovado')
elif 5 <= media < 7:
    print('\033[33m Recuperação')
else:
    print('\033[32m Aprovado')
    print('\033[1:35:40m PARABENS!!! CLATAPLUK *fogos de artificio*\033[0m')
