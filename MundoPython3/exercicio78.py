lista = list()
cont1 = cont2 = 0
for v in range(0, 5):
    lista.append(int(input(f"Digite um número na posição {v}:")))

for p, a in enumerate(lista):
    if cont1 >= 1 and a == max(lista):
        print(f" e {p}", end="\n")
    elif a >= max(lista):
        print(f"O maior valor da lista é o número {a} e está na posição {p}", end="")
        cont1 += 1

for p, e in enumerate(lista):
    if cont2 >= 1 and e == min(lista):
        print(f" e {p}", end="\n")
    elif e <= min(lista):
        print(f"O maior valor da lista é o número {e} e está na posição {p}", end="")
        cont2 += 1
