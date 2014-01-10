#!/usr/bin/python
# -*- coding: latin-1 -*-
'''Faça um Programa que verifique se uma letra digitada é vogal ou consoante. 
http://www.python.org.br/wiki/EstruturaDeDecisao'''  
   
print 'Verifique se uma letra digitada é vogal ou consoante. \n'  
   
Valor1 = raw_input("Insira qualquer letra: ")  
Valor1 = Valor1.upper()  
  
if Valor1 in ('AEIOU'):
 print 'Vogal. \n'  
else:  
 print 'Consoante. \n' 