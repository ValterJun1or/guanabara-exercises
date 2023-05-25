from datetime import date

adulto = 0
jovem = 0

for nome in range(1, 8):
    ano = int(input('Digite o ano em que a pessoa nasceu:'))
    if date.today().year - ano >= 21:
        adulto += 1
    elif date.today().year - ano < 21:
        jovem += 1
    else:
        print('\033[33mOcorreu um erro\033[0m')

print('Há {} pessoas que atingiram a maioridade e {} que ainda não.'.format(adulto, jovem))
