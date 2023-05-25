from datetime import date
data = int(input('Digite o ano em que você nasceu:'))
idade = date.today().year - data

if idade > 18:
    print('\033[31m Você passou do prazo para se alistar. \033[0m')
    prazo = idade - 18
    if prazo == 1:
        print('( \033[33m Você devia ter se alistado há {} ano atrás. \033[0m )'.format(prazo))
    else:
        print('( \033[33m Você devia ter se alistado há {} anos atrás. \033[0m )'.format(prazo))

elif idade < 18:
    print('\033[36m Você ainda não tem idade para se alistar.\033[0m')
    prazo = 18 - idade
    if prazo == 1:
        print('( \033[33m Você deverá se alistar em {} ano! \033[0m )'.format(prazo))
    else:
        print('( \033[33m Você deverá se alistar em {} anos! \033[0m )'.format(prazo))

elif idade == 18:
    print('\033[32m Você está na idade para se alistar.\033[0m')
