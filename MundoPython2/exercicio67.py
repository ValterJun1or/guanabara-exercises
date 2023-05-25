mult = resul = cont = num = 0
while True:
    num = int(input("Qual tabuada até 10 você deseja conhecer?"))
    if num < 0:
        break
    while True:
        cont += 1
        mult += 1
        resul = num * mult
        print(f"{num} x {mult} = {resul}")
        if cont == 10:
            mult = resul = cont = 0
            break
    print("=-=-=" * 10)

# solução mais simples
"""while True:
    num = int(input("Qual tabuada até 10 você deseja conhecer?"))
    if num < 0:
        break
    for mult in range(1, 11):
        print(f"{num} x {mult} = {num * mult}")"""