from datetime import date
print('Descubra se o ano é ou não bissexto e se quiser saber se o ano atual é bissexto então digite 0')
ano = int(input('Escreva um ano:'))
if ano == 0:
    ano = date.today().year
if (ano % 4) == 0 and (ano % 100) != 0 or (ano % 400) == 0:
    print('Esse ano é bissexto')
else:
    print('Esse ano não é bissexto')

