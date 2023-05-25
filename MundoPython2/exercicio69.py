cont_idad = cont_sex = cont_f20 = cont_pes = 0
print("-=-" * 10)
print("CADASTRE UMA PESSOA")
while True:
    print("-=-" * 10)
    idade = int(input("Digite a idade:"))
    sexo = str(input("Digite o sexo[M/F]:")).upper().strip()[0]
    cont_pes += 1
    if idade >= 18:
        cont_idad += 1
    if sexo in 'Mm':
        cont_sex += 1
    if sexo in 'Ff' and idade < 20:
        cont_f20 += 1
    print("-" * 30)
    resposta = str(input("Deseja continuar?[S/N]")).upper().strip()[0]
    if resposta not in 'Ss':
        break
print("-~-" * 10)
print(f"{cont_pes} PESSOAS FORAM CADASTRADAS!!!")
print("-~-" * 10)
print(f"{cont_idad} pessoas tem mais de 18 anos.")
print(f"{cont_sex} pessoas são do sexo masculino.")
print(f"{cont_f20} mulheres tem menos de 20 anos.")
