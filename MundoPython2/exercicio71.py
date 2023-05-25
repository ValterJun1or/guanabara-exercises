ced_50 = ced_20 = ced_10 = ced_1 = 0

print("*" * 37)
print("\033[35mBEM-VINDO AO CAIXA ELETRÔNICO VIRTUAL\033[0m")
print("*" * 37)

while True:
    valor = int(input("Qual valor você deseja sacar:R$"))
    while valor >= 50:
        valor -= 50
        ced_50 += 1

    while valor >= 20:
        valor -= 20
        ced_20 += 1

    while valor >= 10:
        valor -= 10
        ced_10 += 1

    while valor >= 1:
        valor -= 1
        ced_1 += 1

    if valor == 0:
        break

print("\033[36mVocê receberá:\033[0m")
if ced_50 != 0:
    print(f"{ced_50} notas de R$50")
if ced_20 != 0:
    print(f"{ced_20} notas de R$20")
if ced_10 != 0:
    print(f"{ced_10} notas de R$10")
if ced_1 != 0:
    print(f"{ced_1} notas de R$1.")

print("\033[36m{:-^38}".format('FIM'))
