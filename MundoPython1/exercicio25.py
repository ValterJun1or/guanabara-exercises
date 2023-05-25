nome = input('Digite um nome:').strip()
if 'SILVA' in nome.upper():
    print("Seu nome contém \033[35mSilva\033[0m")
else:
    print("Seu nome não contém \033[35mSilva\033[0m")
