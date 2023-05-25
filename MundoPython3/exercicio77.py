tupla = ('One Piece', 'chocolate', 'python', 'Monster', 'Agua')

for palavra in tupla:
    print(f"Para a palavra \033[35m{palavra}\033[0m as suas vogais são:", end='\n')
    for i in range(0, len(palavra)):
        if palavra[i] in 'aeiouAEIOU':
            print(palavra[i])
    print('-' * 40)
print("Fim!")
