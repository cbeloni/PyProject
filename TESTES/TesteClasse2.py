#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Personagem:
   """ Classe que cria personagens do jogo """
   def __init__(self,Nome,Poder):
       """ Método construtor da classe, onde recebe os parametros Nome e Poder de cada bonequinho """
       self.Nome = Nome
       self.Poder = Poder
       print 'Criando personagem ',Nome,' com poder ',Poder
   def Correr(self):
       print self.Nome,' esta correndo'
   def Chute(self,Adversario):
       print self.Nome,' Deu um chute em ',Adversario

p = Personagem('Caue', 'voar')       
p.Correr()
p.Chute('Gi')