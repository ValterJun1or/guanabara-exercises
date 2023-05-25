from time import sleep
primeiro = int(input('Digite o primeiro termo da sua progressão aritmétrica:'))
razao = int(input('Digite a razão da sua progressão aritmétrica:'))
termo = primeiro
cont = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo}, ' if cont < total else f'{termo}.', end='')
        termo += razao
        cont += 1
        sleep(0.2)
    mais = int(input("\n\033[32mQuantos termos você deseja mostrar a mais?\033[0m"))
print(f"A quantidade de termos foi igual a \033[34m{total}\033[0m")

res = int(input("\n\033[35mQuer ver mais alguma progressão aritmetica?\033[0m \n Se sim digite 1, se não digite 0:"))

while res != 0:
    primeiro = int(input('Digite o primeiro termo da progressão aritmétrica:'))
    razao = int(input('Agora a razão dela:'))
    termo = primeiro
    cont = 1
    total = 0
    mais = 10

    while mais != 0:
        total += mais
        while cont <= total:
            print(f'{termo}, ' if cont < total else f'{termo}.', end='')
            termo += razao
            cont += 1
            sleep(0.2)
        mais = int(input("\n\033[32mQuantos termos você deseja mostrar a mais?\033[0m"))
    print(f"A quantidade de termos foi igual a \033[34m{total}\033[0m")

    res = int(input("\n\033[35mDeseja ver mais alguma?\033[0m \n Se sim digite 1, se não digite 0:"))

print("\n\033[34mFim.\033[0m")
