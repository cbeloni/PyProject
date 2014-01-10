#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Pessoa(object):
    FEMALE = 0
    MALE = 1

    def __init__(self, nome, sexo):
        super(Pessoa, self).__init__()
        self._nome = nome
        self._sexo = sexo

    def __str__(self):
        return str(self._nome)

class Pais(Pessoa):

#    def __init__(self, nome, sexo, crianca):
#        super(Pais, self).__init__(nome, sexo)
#        self._crianca = crianca

    def getCrianca(self, i):
        return self._crianca[i]

    def __str__(self):
        pass

p = Pessoa('Beloni', 'Masc')
q = Pais('caue', 'm')
print p._nome
print q._sexo
