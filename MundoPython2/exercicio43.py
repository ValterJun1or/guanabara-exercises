peso = float(input('Digite seu peso:'))
altura = float(input('Digite sua altura:'))
imc = peso / (altura ** 2)

if imc < 18.5:
    print('Você está\033[31m abaixo do peso ')
elif 18.5 <= imc <= 25:
    print('Você está no\033[32m peso ideal')
elif 25 < imc <= 30:
    print('Você está no\033[33m sobrepeso')
elif 30 < imc <= 40:
    print('Você está\033[34m obeso')
else:
    print('Você está na\033[35m obesidade mórbida')

print('\033[36mBeba água e tenha uma vida saudável <3')
