#!/usr/bin/python3

###############################
### EXERCICIO FUNÇÕES
###############################

# Criar uma função de soma que retorna a soma de 2 valores
# Criar uma função de subtração que retorna a subtração de 2 valores
# Criar uma função de multiplicação que retorna a multiplicação de 2 valores
# Criar uma função de divisão que retorna a divisão de 2 valores
# Criar uma função que gera raiz quadrada de um número x


def matematicas():
    print('Escolha a opção: ')
    print('1 - SOMA')
    print('2 - SUBTRAÇÃO')
    print('3 - MULTIPLICAÇÃO')
    print('4 - DIVISÃO')
    print('5 - RAIZ QUADRADA')
    return input('digite a opção desejada: ')

def soma(num1,num2):
    print('Você está na função Soma'),
    num1=int(input(print('Insira o primeiro número: ')),
    num2=int(input(print('Insira o segundo número: ')),
    resultado = num1*num2
    return resultado

def multiplicacao():
    print('Você está na função Multiplicação'),
    num1=int(input(print('Insira o primeiro número: ')),
    num2=int(input(print('Insira o segundo número: ')),
    resultado = num1*num2
    return resultado
    



# def consultar_saldo():
#     print('Saldo é R$ x')

# def abrir_caixa():
#     print('Abrindo')

# def fechamento():
#     print('Fechando')

while True:
    print ('OPERAÇÕES MATEMÁTICAS')
    opcao = matematicas()
    if opcao == '1':
        soma() 
    elif opcao == '2':
        subtracao()
    elif opcao == '3':
        multiplicacao() 
    elif opcao == '4':
        fechamento() 
    elif opcao == '5':
        raiz() 
    else:
        break 
    print(resultado)
    input()           
