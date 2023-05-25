from datetime import date
idade = date.today().year - int(input('Em que ano você nasceu?'))

if idade <= 9:
    print('Sua categoria é\033[31m Mirim')
elif idade <= 14:
    print('Sua categoria é\033[32m Infantil')
elif idade <= 19:
    print('Sua categoria é\033[33m Junior')
elif idade <= 20:
    print('Sua categoria é\033[34m Sênior')
else:
    print('Sua categoria é\033[35m Master')
