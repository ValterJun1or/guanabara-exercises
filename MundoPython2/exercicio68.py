from random import randint

resposta = str(input("Par ou Impar?(P/I)")).upper().strip()[0]
vtrs = numPlayer = numIA = soma = 0

while True:
    while resposta not in 'PI':
        resposta = str(input("Par ou Impar?(P/I)")).upper().strip()[0]
    numplayer = int(input("Digite um número:"))
    if numPlayer < 0:
        print("")
        break

    numIA = randint(0, 10)
    print(f"O computador escolheu {numIA}")
    soma = (numIA + numplayer) % 2
    if resposta == "P":
        if soma == 0:
            print("Par!")
            print("Você ganhou!!!")
            vtrs += 1
        
        elif soma == 1:
            print("Impar!")
            print("Você perdeu!!!")
            print(f"Você ganhou um total de {vtrs} vezes.")
            break

    elif resposta == "I":
        if soma == 0:
            print("Par!")
            print("Você perdeu!!!")
            print(f"Voce ganhou um total de {vtrs} vezes.")
            break
        elif soma == 1:
            print("Impar!")
            print("Você ganhou!!!")
            vtrs += 1
