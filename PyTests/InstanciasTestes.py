#!/usr/bin/env python
# -*- coding: utf-8 -*-
class A:
   a = 1 # atributo publico
   __b = 2 # atributo privado a class A
 
class B(A):
   __c = 3 # atributo privado
 
   def __init__(self):
     print self.a
     print self.__c
a = A()
print isinstance(a, B) # ''Objeto a'' é uma instância da ''classe B''? Falso.
 
a = B() # Instancía o ''objeto a'' na ''classe B'' e imprime os atributos da classe.
print isinstance(a, B) # ''Objeto a'' é uma instância da ''classe B''?Verdadeiro.
 
b = B() # Instancía o ''objeto b'' na ''classe B'' e imprime os atributos da classe.
print isinstance(b, B) # ''Objeto b'' é uma instância da ''classe B''? Verdadeiro.
 
b = A() # Instancía o ''objeto b'' na ''classe A''.
print isinstance(b, A) # ''Objeto b'' é uma instância da ''classe A''? Verdadeiro.

