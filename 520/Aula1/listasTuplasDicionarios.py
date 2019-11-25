#! /usr/bin/python3

lista = ['Arroz','Feijão','Óleo','Sal','Açucar','Temperos'] #criando lista
#           0        1       2     3      4          5
print(lista)

#Se quero acessar o primeiro item da lista (toda contagem de lista começa por '0')
print(lista[0]) 
#Indice '-1' pega o ultimo que é 'Temperos'
print(lista[-1]) 
#Indice '-2' pega o penultimo que é 'Açucar'
print(lista[-2]) 

#parametro ':' que defini inicio, fim e passo (do 0 em diante)
print(lista[0:]) 

#parametro ':' que defini inicio, fim e passo (do 1 em diante)
print(lista[1:]) 

#parametro ':' que defini limite (do 1 ao 4, coloca 1 indice a mais que é o '5')
print(lista[1:5:]) 

 #parametro ':' que defini filtragem ('1' inicio, '4' fim, '2' passo (filtragem))
print(lista[1:4:2])


#EXERCICIO - CRIAR UMA LISTA COM 5 ELEMENTOS, SEMPRE PEGAR O PENULTIMO ITEM DA LISTA

listaexercicio = ['Azul','Vermelho','Verde','Amarelo','Preto','Cinza']

print(listaexercicio[-2])

listaexercicio = ['Azul','Vermelho','Verde','Amarelo','Preto','Cinza','Roxo']

print(listaexercicio[-2])

# LISTAS VETORES MULTIDIMENSIONAIS
# são listas que contem listas, ou MATRIZES

lista3d = [
    [2 , 3 , 4 , 5],             #separando as listas por virgula, que podem ter outras listas dentro
    [3 , 4 , 5 , 6],
    [7 , 5 , 7 , 8]
]

#para acessar o 7 da terceira lista
print(lista3d[2][2])   

lista3d = [
    [2 , 3 , 4 , 5],             
    [3 , 4 , 5 , 6],
    [7 , 5 , 7 , 8],
    [x for x in range(100)]
]

print(lista3d)  

#METODOS DE LISTA

#adiciona dentro do meu codigo mais um item que é 'Carne'
lista.append('Carne') 

#imprime a lista com 'Carne' adicionada
print(lista) 

# define para inserir 'Sabão em Pó' no índice '0'
lista.insert(0,'Sabão em Pó') 

print(lista)

#remove sempre o ultimo elemento da minha lista se deixar em branco '-1', se colocar numero remove o item da posição ex: 4
lista.pop(4)    

print(lista)

#organiza minha lista no caso do sort, quando dar um print ordena em ordem alfabetica/numerica
lista.sort() 

print(lista)

#organiza minha lista no caso do reverso
lista.reverse() 
print(lista)

#imprime o tamanho da minha lista
print(len(lista)) 

#buscar determinado indice na minha lista e saber onde está 'Açucar'- retorna índice '5' como Açucar
print(lista.index('Açucar')) 

#retorna a quantidade de itens com o nome 'Arroz' no meu código
print(lista.count('Arroz')) 

#remove sempre o primeiro índice 'Óleo' da ocorrência
print(lista.remove('Óleo')) 
print(lista)

#trocar um certo indice por outro item

lista[3] = 'Maça'
print(lista)

######################
## TUPLAS
#####################

#TUPLAS são como listas, mas mutaveis
#primeiro metodo
tupla = ('Maça','Banana','Laranja','Abacaxi','Uva')
print(type(tupla))

#segundo metodo para criar tuplas
tupla2 = 'valor1' , 2, True, 2j
print(type(tupla2))

#colocar um novo item na tupla (não eh mutavel), a tupla serve como lista fixa dentro do python
#  tupla[5]='Manga' (nao deixa agregar, nem mexer na tupla)

print(tupla)

#vai mostrar em qual item esta a 'Banana'
print(tupla.count('Banana')) 

print(tupla)

#acessando indices de uma tupla
print(tupla[3])
print(tupla[1:4])
print(tupla[-2])

#converter uma tupla em uma lista
lista_da_tupla = list(tupla)

print(lista_da_tupla)

print(tupla)

#uma lista dentro da tupla, se torna um elemente imutavel

#criando uma lista dentro da tupla
tupla = (['Indice 1'], 'Nome')
#acessando o indice '0' que é uma lista e adicionando um item 'Indice 2'
tupla[0].append('Indice 2')
print(tupla)



###################
##### DICTIONARIES
###################

#DICIONARIO   ----- CHAVE -----VALOR
#                   CACHORRO --ANIMAL DA FAMILIA....

# NOME: DANIEL
# SOBRENOME: SILVA
# LOCAL_DE_TRABALHO: 4LINUX

# Similaridade com a estrutura do JSON


#Criando um dicionario
apresentacoes={
    'Paulista' : 'Salve',
    'Carioca' : 'Vai Flamengo',
    'Pirata' : 'Argh',
    'Mineiro' : 'Pão de queijo',
    'Acreano' : 'Barulhos de Dinossauros',
}

#acessando indices em um dicionario
print(apresentacoes['Paulista'])

#criando um dicionario com multi-valores internos
linguagem_favorita = {
    'Daniel' : {
        'linguagem' : 'Python',
        'Tempo_de_experiencia' : 5,
    },
    'Olympio'  : {
        'linguagem' : 'R',
        'linguagem2': 'VBA',
        'Tempo_de_experiencia' : 10,
    },
    'Leandro'  : {
        'linguagem' : 'Zabbix',
        'linguagem2': 'Linux',
        'Tempo_de_experiencia' : 2,
    },
}

#exibe o dicionario completo
print(linguagem_favorita.get('Daniel'))

#exibe somente a 'linguagem'
print(linguagem_favorita.get('Daniel')['linguagem'])

#acesso a todas as chaves
print(linguagem_favorita.keys())

#acesso aos valores
print(linguagem_favorita.values())

#acesso aos itens
print(linguagem_favorita.items())

valores = {'nome':'Daniel','Sobrenome':'Silva'}
print(valores.items())


###################
### Números
##################

#Operações matemáticas

somar = 2+2
print (2 + 2 , 'Retornando o valor de 2+2')
print (somar, 'Retornando somar')

subtrair = somar - 2 #somar retonra um tipo inteiro
print (subtrair, 'Retornando subtrair')

multiplicar = subtrair * 3 # subtrair tb retorna um tipo inteiro
print (multiplicar, 'Retornando multiplicar')

divisao = multiplicar / 5 # multiplicar tb retorna um tipo inteiro
print(divisao, 'Retornando dividir') #retorna um valor de ponto flutuante

potencia = 2**2   # 2 elevado a 2
print(potencia, 'Retornando potencia') #retorna um valor tipo inteiro

raiz = 2**0,5   # raiz 2 elevado a 0,5
print(raiz, 'Retornando raiz') #retorna um valor tipo inteiro

letras = 'abcdefghijk' #somando dois itens
print(letras[0])  #exibe o indice '0' das letras

letras = 'abcdefghijk' + 'lmnopqrstuvxyz' #somando dois itens
print(letras) 

print(input('Digite um numero: ') + input('DIgite Outro Numero: ')) #concatena os numeros

print(float(input('Digite um numero: ')) + float(input('DIgite Outro Numero: '))) #soma 2 numeros em ponto flutuante

