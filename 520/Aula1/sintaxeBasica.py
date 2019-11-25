#! /usr/bin/python3

# print ('hello world')
# input ("digite seu nome: ")
# print (input ('Digite seu nome: '), 'Seja bem vindo')

# print (input ('Digite sua Idade: '), 'anos, Essa é sua idade')

nome=input('Digite seu nome: ')
#print (nome , ', esse é seu nome.')

#print ('Seu nome é' , nome)

#print (f'Seu nome é {nome}')

# print ('Seu nome é {0}'.format(nome))

# tipos de variáveis

texto = '4linux' #string
numero = 3 # int
numero_real = 3.6 #float
numero_complexo= 2j #variavel de numero complexo
CONSTANTE = 3.14 # Representação em código de constante
booleanas = True # bool -> Verdadeiro e Falso
listas = ['item1','item2','item3'] #list
tuplas = ('item1','item2','item3') #tuple
tupla2 = 'item1','item2' #tupla
dicionarios = {'nome':'Leandro','sobrenome':'Silva'} #dict

idade = input('Digite sua idade: ')
#print(f'{nome} Sua idade é {idade} anos')


# print('{} Sua idade é {} anos'.format(nome, idade))

# print('{1} Sua idade é {0} anos'.format(nome, idade)) # indexa valores à ordem declarada

print(nome,idade,sep='.',end='\n\n') #exibe funcoes concatenadas com . entre elas e pula 2 linhas

print(type(texto.lower))

print(texto.lower())
print(texto.upper())
print(texto.title())
print(texto.strip())
print(texto.replace('l','p'))


# email = input('Digite um E-mail: ')         
# email = str(input('Digite um E-mail: '))    # converte todo o dado numerico em texto

#print(email)

# email = str(input('Digite um E-mail: ')).lower() #converte todo o dado em minusculas
email = str(input('Digite um E-mail: ')).lower().strip() #converte todo o dado em minusculas e retira os espaços

print(email)

