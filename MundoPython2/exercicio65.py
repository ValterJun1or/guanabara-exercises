print("Saiba a média e quais foram os maiores e menores números digitados!!!")

maior = quant = menor = num = media = soma = 0
resposta = " "

while resposta not in "Nn":
    numero = int(input("Digite um número:"))
    quant += 1
    soma += numero
    if quant == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero

    resposta = str(input("Deseja continuar? (S/N)")).upper().strip()[0]

media = soma / quant

print(f"Você digitou {quant} e a média dos números foi {media}.")
print(f"O maior número foi {maior},o menor foi {menor}.")
