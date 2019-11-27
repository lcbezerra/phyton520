#!/usr/bin/python3

#############################
#### ESCOPO DE VARIÁVEL
############################

variavel = 3

print(variavel)

def muda_variavel():
    global variavel    #'global' usa para definir que a variavel a ser mudada é geral do código
    # variavel = 2       # variavel no escopo local
    print(variavel)

muda_variavel()

print(variavel)