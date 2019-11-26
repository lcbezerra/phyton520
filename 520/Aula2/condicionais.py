#!/usr/bin/python3

#######################
## Estrutura de condicional simples
#######################


nome = input('Digite seu nome: ')

if nome == 'Daniel':
    print('Olá professor')

print('Seja bem vindo, você pode utilizar a plataforma')


#######################
## Estrutura de condicional composta
#######################

nome = input('Digite seu nome: ')

if nome == 'Daniel':
    print('Olá professor')
else:
    print(f'Olá aluno {nome}')
print('Seja bem vindo, você pode utilizar a plataforma')


####
carro = input('Digite qual o caminho a ser seguido (engarrafado ou livre): ')

a = 'engarrafado'
b = 'livre'

if a == 'engarrafado':
    print('Melhor ir pela b')
else:
    print('Indo pelo caminho a')


################
## Comparando duas condições
################

nome = input('Digite seu nome: ').strip().title()            #Strip tira espaço do começo // title coloca a primeira letra maiuscula
sobrenome = input('Digite seu sobrenome: ').strip().title()

if nome == 'Daniel' and sobrenome == 'Silva': #pode-se utilizar o 'or'
    print(f'Olá professor {nome} {sobrenome}')
else:
    print(f'Olá aluno {nome} {sobrenome}')
print('Seja bem vindo, você pode utilizar a plataforma')

##########################
#### Condicionais encadeadas
############################

if nome == 'Daniel':
    if sobrenome == 'Silva':
        print('Olá professor')
    else:
        print('Você é Daniel, mas não é o professor')
else:
    print(f'Olá aluno {nome} {sobrenome}')

############################
##### Condicionais aninhadas
############################

print('\n\nAULA ELIF\n\n')

nome = input('Digite seu nome: ').strip().title()            #Strip tira espaço do começo // title coloca a primeira letra maiuscula
sobrenome = input('Digite seu sobrenome: ').strip().title()

if nome == 'Daniel':
    print(f'Seu nome é muito bonito, {nome} {sobrenome}')
elif nome == 'Juliana':
    print(f'Seu nome é bem legal, {nome} {sobrenome}')
elif nome == 'Jorge':
    print(f'Seu nome é muito feio, {nome} {sobrenome}')
else:
    print(f'Seu nome é bem normal {nome} {sobrenome}')

