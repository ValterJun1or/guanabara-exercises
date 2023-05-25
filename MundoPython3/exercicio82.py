l_mae = list()
l_par = list()
l_impar = list()
while True:
    n = int(input("Digite um número:"))
    l_mae.append(n)
    pergunta = str(input("Quer digitar outro número?")).lower()
    if pergunta in 'n não nao':
        break
for i in range(0, len(l_mae)):
    if (l_mae[i] % 2) == 0:
        l_par.append(l_mae[i])
    elif (l_mae[i] % 2) == 1:
        l_impar.append(l_mae[i])
print(l_mae, l_par, l_impar)

"""Ao invés de usar "l_mae" troque o for i in range por for i, v in enumerate(l_mae),
assim o termo "l_mae" muitas vezes repetido pode ser trocado pelo v criado pelo for"""