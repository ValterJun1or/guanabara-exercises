CMF = (
      'Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino', 'Fluminense', 'América-MG',
      'Atlético-GO', 'Santos', 'Ceará SC', 'Internacional', 'São Paulo', 'Athletico-PR', 'Cuiabá', 'Juventude',
      'Grêmio', 'Bahia', 'Sport Recife', 'Chapecoense'
      )
print(f'Brasileirão 2020:{CMF}')
print(20 * '-=-')
print(f'Os cinco primeiros colocados:{CMF[0:6]}')
print(30 * '-')
print(f'Os quatro últimos colocados:{CMF[-4:]}')
print(30 * '-')
print(f'Em ordem alfabetica:{sorted(CMF)}')
print(30 * '-')
print(f'Chapecoense está na {(CMF.index("Chapecoense")) + 1}º posição.')
