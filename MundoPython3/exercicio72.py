numeros = (
    'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
    'onze', 'doze', 'treze', 'quartoze', 'quinze', 'dezesseis', 'dessezete', 'dezoito', 'dezenove', 'vinte'
      )
num = int(input('Digite um número entre 0 e 20 para aparecer em extenso:'))
while -1 >= num or num >= 21:
    print("Erro.", end='')
    num = (int(input("Tente digitar um número entre 0 e 20 dessa vez:")))

print(f"Você escreveu o número {numeros[num]}.")
