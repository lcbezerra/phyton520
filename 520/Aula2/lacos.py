#!/usr/bin/python3

#########################
### Laço WHILE
### Laços de repetição
########################

# Este laço executa enquanto uma condição for verdadeira

i = 0
while ( i < 10): # Enquanto i for menor que 10
    print(i)     # mostra valor de i
    i += 1       # i = i + 1
    #repete

# Como fazer o controle de um loop while

i=0
while(True):
    print('Teoricamente, um loop infinito')
    i += 1
    if i == 3:
        break

#PARTE 2

# i=0
# while(True):
#     i += 1
#     if i == 10:
#         break
#     if i == 5:
#         continue
#     print('Teoricamente, um looping infinito')

# Continue retoma do começo a execução de um looping (testando pares)
i=100               # numero inicial (Iterador regressivo)
while i > 0:        # Enquanto i < 0
    i -= 1          # i = i - 1
    if i % 2 == 1:  # testa os modulos de divisao 
        continue
    print(i)


#################
### LAÇO FOR
#################
#Percorre itens em determinado alcance de valores

for i in range(1,100,2): #Começa do 1, vai até o 100 de 2 em 2
    print (i)

lista = []
for i in range(1,100,2):    #Começa do 1, vai até o 100 de 2 em 2
    lista.append(i)         #insere os valores de i na lista

print(lista)

i = 1
lista = []
for i in range(1,100,1):    #Começa do 1, vai até o 100 de 1 em 1
    lista.append(i)         #insere os valores de i na lista

print(lista)

for i in lista:    #Começa do 1, vai até o 100 de 2 em 2
    if i % 2 == 0:
        print(f'\033[31m{i}\033[0m', 'par') #escreve i em vermelho
    if i % 2 == 1:
        print(f'\033[32m{i}\033[0m', 'impar') #escreve i em verde

# Percorrer um dicionário

dicionario = {
'nome':'Daniel',
'sobrenome':'Silva',
}

for i in dicionario:        # Percorre dicionario
    print(dicionario[i])

for chave,valor in dicionario.items(): # percorre docionario, em chaves e valor
    print(chave)                        #printa chaves
    print(valor)                        #printa valor

#### ENUMERANDO ITENS DE UMA LISTA
lista = ['item1', 'item2' , 'item3' , 'item4' , 'item5' , 'item6' , 'item7' , 'item8' ,]

print(list(enumerate(lista))) # enumera lista agregando numero ao item

for i in enumerate(lista): #enumera lista pelo for
    print(i)

for indice,valor in enumerate(lista):
    print(valor)

#list comprehension (compreensão de listas)
lista = [x for x in range (1,100)]
print(lista)

