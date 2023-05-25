print("-" * 30)
print("ADICIONE OS PRODUTOS AQUI")
print("" * 30)

total = prod_1000 = prod_barato = 0
nome_barato = ''

while True:
    nome_prod = str(input("Nome do produto:"))
    preco_prod = float(input("Preço do produto:"))
    total += preco_prod

    if preco_prod > 1000:
        prod_1000 += 1

    if prod_barato == 0 or preco_prod < prod_barato:
        prod_barato = preco_prod
        nome_barato = nome_prod

    resposta = str(input("Deseja adicionar mais algum produto?[S/N]")).upper().strip()[0]
    while resposta not in 'SsNn':
        resposta = str(input("Deseja adicionar mais algum produto?[S/N]")).upper().strip()[0]
    if resposta in 'Nn':
        break

print(f"Você gastará no total \033[33mR${total:.2f}\033[0m.")
print(f"\033[33m{prod_1000}\033[0m produtos custam mais de R$1000")
print(f"O nome do produto mais barato é \033[33m{nome_barato}\033[0m e custa \033[33mR${prod_barato:.2f}\033[0m")
