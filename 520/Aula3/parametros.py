#!/usr/bin/python3
'''


'''


########################
## PARÂMETROS DE FUNÇÃO
########################

def retorna_pessoa(nome,idade=99):
    print(f'Nome: {nome}\nidade: {idade}')

retorna_pessoa(nome='Daniel', idade=19)

##################
# Especificar tipo de parâmetro e retorno

### ANotações de função

def retorna_valor_int( inteiro : int)-> int:
    ''' Função com anotação de tipo
    
    Se refere a função que possui tipos específicos e
    mostram na sua sintaxe de construção o que é necessaŕio,
    sempre tem que pular uma linha'''



def retorna_valor_int( inteiro : int, booleano: bool):
    return inteiro


### args e Kwargs
print('olá' , 'mundo' , ',' , 'prazer' , 'sou' , 'Daniel')

## Criando uma função que recebe multiplos valores - Args
def funcao_multi_valores(parametros_estaticos,*argumento_variavel): #coloca '*' para tornar o argumento variavel
    print(parametros_estaticos, 'parâmetro estático')
    print(argumento_variavel)
    # Fazendo acesso aos parâmetros
    # for argumento in argumento_variavel:
    #     print(argumento)

funcao_multi_valores('valor estatico obrigatório',
                    'Daniel','Andressa', 'João','Ana'
                    'Paula','Lucas','Leonardo','Pedro')


# Argumentos com palavra chave - kwargs

def parametros_chave_valor(**dados):
    if dados['nome'] == 'Daniel':
        print('Acesso Negado')
    else:
        print('Permitido')
    #print(dados)

# Execução - método 1
print('***** Método 1 *******')
parametros_chave_valor(nome='Daniel',sobrenome='Silva',
                        idade=19,sexo='Masculino')

# Execução - método 2    
print('***** Método 2 *******')
dados_requisicao = {'nome':'Daniel',
                    'sobrenome':'Silva',
                    'Profissão':'Operador de empilhadeira'}

parametros_chave_valor(**dados_requisicao)
