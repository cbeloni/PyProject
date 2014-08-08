#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from random import randint
valor = []
y = 0
#jogo = [13, 24, 35, 39, 47, 58]
jogo = [13, 24, 35, 39, 47, 58]
nao_acertou = True
tentativas = 0

while nao_acertou:
	valor = []
	y = 0    
	while y != 6:
		novo_numero = randint(1,60)
		if novo_numero not in valor:
			valor.append(novo_numero)
			y += 1
			
	ordenado = sorted(valor, key=int)

	if ordenado != jogo:
		tentativas += 1
	else:
		nao_acertou = False

	if tentativas % 100000 == 0:
		print ("mais 100000 tentativas!!")
		print (tentativas)
		print (jogo)
		print (ordenado)

print (jogo)
print (ordenado)
print (tentativas)
