#!/usr/bin/python3

###################################
## MANIPULANDO ARQUIVOS COM PYTHON
###################################

######## Abrir um arquivo para modificação

######## Método não recomendado ##########

ponteiro = open('nomedoarquivo.txt','a')
#Abre um ponteiro para escrita de arquivos
# o modo utilizado é o read plus (que serve para leitura
# e escrita). Possuímos vários modos de acesso, por exemplo:
# w = sobrescrita
# r = somente leitura
# + = abre um arquivo para atualização (acrescenta e modifica)
# a = complemento
# x= criação
# este método não é recomenadado porque o ponteiro sempre necessita
# ser encerrado com o close, isso foi substituído com a adição 
#do comando with (mostraremos em breve)

ponteiro.write('Olá mundo\n')
#ponteiro.read()
ponteiro.close()

### MÉTODO USUAL ###

#Arquivo em modo de escrita
with open('nomedoarquivo2.txt','a') as arquivo:
    arquivo.write('Olá mundo\n')
    arquivo.writelines(['banana\n','maçã\n'])

#Arruivo em modo de leitura
with open('nomedoarquivo2.txt','r') as arquivo:
    letras = arquivo.readlines()

print(letras)
