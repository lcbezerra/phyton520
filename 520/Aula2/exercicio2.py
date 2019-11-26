#!/usr/bin/python3

# Validar uma entrada com while. Enquanto o usuário não digitar sair ele ficará preso no loop pedindo 'Digite Algo:'

sair = ''

while(not sair == 'sair'):
    sair = input('Digite algo: ')
