#!/usr/bin/env python3

#from Cachorro import Cachorro
import Cachorro


# nome, idade, cor, raca='Vira-lata', porte='Médio'

dados_do_cachorro = {
    'nome':'caozinho',
    'idade':8,
    'cor':'branco',
    'raca':'Poodle',
    'porte':'pequeno'
}

dados_do_cachorro2 = {
    'nome':'rex',
    'idade':10,
    'cor':'caramelo',
    'raca':'Vira-Lata',
    'porte':'Médio'
}

caozinho = Cachorro.Cachorro(**dados_do_cachorro)

caozinho.latir()
caozinho.cheirar()
caozinho.latir()
caozinho.latir()
caozinho.cagar()

print(caozinho.patas)
print(caozinho.lingua)

caozinho.lingua = False

caozinho.latir()

rex = Cachorro.Cachorro(**dados_do_cachorro2)
rex.latir()


input()                  # Interrompe a execução e fica pausado


