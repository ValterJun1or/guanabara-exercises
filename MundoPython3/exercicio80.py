lista = []

for i in range(0, 5):
    num = int(input("Digite um número:"))
    if i == 0:
        lista.append(num)
        print("Primeiro valor adicionado com sucesso.")
    elif num > lista[-1]:
        lista.append(num)
        print("Ultimo valor da lista adicionado com sucesso.")
    else:
        p = 0
        while p < len(lista):
            if num < lista[p]:
                lista.insert(p, num)
                print(f"Valor adicionado na posição {p} com sucesso.")
                break
            p += 1
print(lista)

