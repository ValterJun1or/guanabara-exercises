nome = str(input('Digite seu nome:')).strip()
print('Seu nome todo em maiusculo é:', nome.upper())
print('Seu nome todo em minusculo é:', nome.lower())
pp = nome.split()
print('Há', len(''.join(pp[0])) ,'letras no seu nome')
print('Seu primeiro nome é', pp[0] ,'e ele tem' ,len(''.join(pp[0])) , 'letras')
#Ou
#print('Há', len(''.join(nome.split())),'letras no seu nome')
#print('Seu primeiro nome é:', nome.split()[0])
