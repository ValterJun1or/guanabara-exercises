salario = float(input('Digite o salário em reais:'))
if salario > 1.250:
    print('O salário do funcionário após o aumento é R${:.2f}'.format(salario + (salario * 0.1)))
else:
    print('O salário do funcionário após o aumento é R${:.2f}'.format(salario + (salario * 0.15)))
