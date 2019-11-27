#!/usr/bin/python3

''' Exercício de funções

Essa aula fala sobre criação de funções'''
###############################
### EXERCICIO FUNÇÕES
###############################

# Criar uma função de soma que retorna a soma de 2 valores
# Criar uma função de subtração que retorna a subtração de 2 valores
# Criar uma função de multiplicação que retorna a multiplicação de 2 valores
# Criar uma função de divisão que retorna a divisão de 2 valores
# Criar uma função que gera raiz quadrada de um número x

# Como fazer documentação da sua função
def soma(n1, n2):
    ''' Função de soma


    Este modulo realiza soma com dois valores, e retorna o valor.'''
    print(__doc__)
    return n1 + n2

def subtrair(n1, n2):
    return n1 - n2

def multiplicar(n1, n2):
    return n1 * n2

def dividir(n1, n2):
    if n2 == 0:
        raise ZeroDivisionError('Não se divide um número por 0')
    else:
        return n1 / n2

def raiz(n1):
    if n1 < 0:
        n1 **= 0.5
        return complex(n1)
        #raise ValueError ('Não tem como fazer esse cálculo')
    else:
        return n1 ** 0.5

n1=input('Digite o primeiro número: ')
n2=input('Digite o segundo número: ')
resultado = soma(int(n1),int(n2))
print(resultado)


