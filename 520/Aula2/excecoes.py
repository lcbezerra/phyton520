#!/usr/bin/python3

#########################
### TRATANDO DE EXCEÇÕES
#########################

try:                                     # tenta executar o comando
    print('Soma de dois valores')
    numero1 = int(input('Digite um numero a ser somado: '))
    numero2 = int(input('Digite outro numero a ser somado: '))
    print(numero1 + numero2)

except ValueError:                      # em caso de erro ele faz exceção e exibe a mensagem
    print('Valores indevidos inseridos, insira somente números inteiros')




# DIVISAO

try:                                     # tenta executar o comando
    print('Soma de dois valores')
    numero1 = int(input('Digite um numero a ser dividido: '))
    numero2 = int(input('Digite outro numero a ser o divisor: '))
    print(numero1 / numero2)

except ValueError:                      # em caso de erro ele faz exceção e exibe a mensagem
    print('Valores indevidos inseridos, insira somente números inteiros')

except ZeroDivisionError:
    print('Impossivel dividir por 0')

except Exception as e:                         #Exception para qualquer erro ele trata, e vai gravar na variavel 'e'
    print('Erro na execução do programa' , e)   #mostra na mensagem o codigo de erro 'e'
finally:
    print('Saindo do script')

# nulo = None # serve para zerar o valor de uma variavel


######################################
#### COMO CRIAR EXCEÇÕES
#####################################

print('\n Teste de criação de exceção \n')

#try:
opcao = input('Não digite 5:')
if opcao == '5':
    raise ValueError('Eu falei pra não digitar 5')

#except ValueError as e:
#    print('Deu erro: ', e)