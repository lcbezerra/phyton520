#!/usr/bin/python3

###########################
#### Exercicio de exceções
###########################

# Criar uma tela de cadastro de um usuário em uma lista
# Essa tela não pode aceitar figuras públicas que geram polêmica
# ex = Bolsonaro, Lula, Adolf Hitler, Frota
# Esse loop é infinito, onde só acaba quando colocado uma figura pública

#!/usr/bin/python3

#######
## Exercicio de excessões
#######

# Criar uma tela de cadastro de usuário em uma lista
# Essa tela não pode aceitar figuras públicas que geram polêmica
# ex = Bolsonaro, Lula, Adolf Hitler, Tiririca
# Esse Loop é infinito, onde só acaba quando colocado uma figura
# pública

# Arrays de nomes de figura publica
bolsonaro = [
    'bolsonaro',
    'bozo',
    'bolsanario',
    'borsalino',
    'bonoliro',
    'facista'
    ]
lula = [
    'lula',
    'mula',
    '9 dedos',
    'nove dedos',
    'ladrão',
    'luladrão'
    ]
hitler = [
    'adolf hitler',
    'hitler',
    'fuhr',
    'bigodin',
    'nazista',
    'argentino'
]
tiririca = [
    'tiririca',
    'palhaço',
    'tiririca',
    'florentina'
]

#Atribuindo todas as figuras públicas para uma lista
figuras_publicas = [bolsonaro, lula, hitler, tiririca]

#Atribuindo todos os apelidos a um arquivo de texto
for figura in figuras_publicas:
    for apelido in figura:
        with open('politicos.txt','a') as arquivo:
            arquivo.write(apelido + '\n')
    
#definindo lista de nomes
lista_nomes = []