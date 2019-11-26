#!/usr/bin/python3

######################
##### OPERADORES ARITMÉTICOS
#####################

#### Variáveis por nomenclatura podem ter no máximo 16 caracteres

num1=6
num2=8

#Adição
adicao=num1+num2
print(adicao)

#Subtração
subtracao=num1-num2
print(subtracao, 'resultado da adição')

#Multiplicação
multiplicacao=num1*num2
print(multiplicacao, 'resultado da multiplicacao')

#Divisão
divisao=num1/num2
print(divisao, 'resultado da  divisao')

#Resultado da divisão inteira
result_div_int= num1 // num2
print(result_div_int, 'resultado da divisao por inteiro')

#Resto de uma divisão inteira
resto_div_int= num1 % num2
print(resto_div_int, 'resto da divisao inteira (Módulo)')

#####OPERADORES DE UMA FORMA ABREVIADA
#Pega o valor atual do numero e realiza um cálculo
#Atribuindo o resultado a variavel

numero = 1
numero += 3 # 1+3            numero = numero + 3
numero -= 3 # 4-3            numero = numero - 3
numero *= 4 # 1*4            numero = numero * 4
numero /= 2 # 4/2            numero = numero / 2
numero //= 2 # 2//2=1        numero = numero // 2
numero %= 2 # 2%2 = 0        numero = numero % 2

###########################
### OPERADORES RELACIONAIS
###########################

#Operadores relacionais servem para comparação entre fatores
#Retorna valores booleanos (True or False)

numero1 = 6
numero2 = 9
numero3 = numero1

print(numero1 == numero2)  #Igualdade      - False
print(numero1 != numero2)  #Diferenciação  - True
print(numero1 < numero2)   #Menor que      - True
print(numero1 <= numero2)  #Menor igual    - True
print(numero1 > numero2)   #Maior que      - False
print(numero1 >= numero2)  #Maior igual    - False

print(numero1 is numero3)  #Compara se estão alocados no mesmo bloco de memória - True

lista = ['item1','item2','item3']
print('item1' in lista) #Compara existência de valores em lista - True

