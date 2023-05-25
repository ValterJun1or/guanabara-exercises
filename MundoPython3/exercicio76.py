tot = 0
tupla = ("Feijão", 11.69,
         "Arroz", 8.99,
         "Leite em pó", 15.39,
         "Macarrão", 9.00,
         "Galinha", 23.99,
         "Chocolate", 7.99,
         )
print('-'*36)
print(f'{"Lista dos produtos":^36}')
print('-'*36)

for lista in range(0, len(tupla), 2):
    if lista == 11:
        break
    conta = 30 - len(tupla[lista])
    print(f"{tupla[lista]}{'-' * conta}R${tupla[lista + 1]}")
    tot += tupla[lista + 1]
print(f"Total:{' ' * 24}R${tot}")
print("-"*36)
