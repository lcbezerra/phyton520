#! /usr/bin/python3

mensagem= 'Digite seu nome: '
name=input(mensagem).strip().title() #quando registrar a string ele vai deixar sem espaços e a primeira letra maiuscula

print(f'Seja bem vindo {name}')

print(mensagem.isnumeric()) #vai dizer se minha mensagem é numerica (no caso eh FALSE)

vdd = True

fal= False

print(vdd == False)

print(not(fal == True))

