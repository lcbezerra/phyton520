#!/usr/bin/python3

##################################
### EXERCÍCIO CONDICIONAL COMPOSTA
#################################


#Criar uma variavel idade ode recebe uma idade via linha de comando,
#validar se essa pessoa pode beber ou não, caso possa, atribuir
#ao valor de uma variável embriagado o valor true, se não false

idade_pessoa = int(input('Qual sua idade: '))

# if idade_pessoa >= 18:
#     embriagado = True
# else:
#     embriagado = False

# print('\n\n' , embriagado)

# Criar uma validação para que se a pessoa tiver carteira de motorista, ela possa dirigir.
# Porém criar condicional para que se a pessoa estiver embriagada, mostrar uma mensagem que ela não pode dirigir
# Criar validação Elif para que se a data da pessoa for < 0 indique a mensagem: 'Pessoa Invalida'

if idade_pessoa >= 18:
    cnh = input('Você tem carteira de motorista?(y/n): ').strip().lower()
    if cnh == 'y':
     cnh = True
    else:
        cnh = False
    if cnh == True:
        embriagado = input('Você está embriagado?(y/n):').strip().lower()
        if embriagado == 'y':
            embriagado = True
        else:
            embriagado = False
        if cnh and not embriagado:
            print('Parabéns, você pode dirigir')
        else:
            print('Você não pode dirigir')
    else:
        print('Você não pode dirigir')
elif idade_pessoa <= 0:
    print('Pessoa inválida')
else:
    print('Você não pode dirigir')


##################



