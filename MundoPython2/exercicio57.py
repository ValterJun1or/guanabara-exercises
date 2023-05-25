sexo = str(input('Digite seu sexo(M:masculino / N:feminino):')).strip().upper()
while sexo not in 'MN':
    print('Algo deu errado,novamente', end=' ')
    sexo = str(input('digite seu sexo(M:masculino / N:feminino):')).strip().upper()
