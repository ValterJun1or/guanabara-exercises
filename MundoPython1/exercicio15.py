km = float(input('Quantos km foram percorridos?'))
dia = float(input('Quantos dias ele foi utilizado?'))
vkm = km * 0.15
vdia = dia * 60
vt = vdia + vkm
print('O valor a ser pago será de {:.2f}R$'.format(vt))
print('{:.2f} pelos dias usados e {:.2f} pelos kilometros percorridos'.format(vdia, vkm))
