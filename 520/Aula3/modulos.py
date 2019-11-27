#!/usr/bin/python3


######## Importando nosso próprio módulo
import modulos.calculadora as calculadora   #método 1

from modulos.calculadora import somar       #metodo 2
print (somar(2,3))                          #método 2


from modulos.calculadora import *       #somar, subtrai  #Método 3
print(multiplica(3,9))


soma = calculadora.somar(1,2)

print(soma)

print('Subtração',calculadora.subtrai(5,1))

